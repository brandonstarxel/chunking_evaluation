from .base_chunker import BaseChunker
from chroma_research.utils import openai_token_count
from langchain_text_splitters import RecursiveCharacterTextSplitter
import anthropic
import os
import backoff

# ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_CHROMA_API_KEY')

class AnthropicClient:
    def __init__(self, api_key):
        self.client = anthropic.Anthropic(api_key=api_key)

    @backoff.on_exception(backoff.expo, Exception, max_tries=3)
    def create_message(self, system_prompt, messages, max_tokens=1000, temperature=1.0):
        try:
            message = self.client.messages.create(
                model="claude-3-5-sonnet-20240620",
                max_tokens=max_tokens,
                temperature=temperature,
                system=system_prompt,
                messages=messages
            )
            return message.content[0].text
        except Exception as e:
            print(f"Error occurred: {e}, retrying...")
            raise e
        
class OpenAIClient:
    def __init__(self, api_key, model_name="gpt-4o"):
        from openai import OpenAI
        self.client = OpenAI(api_key=api_key)
        self.model_name = model_name

    @backoff.on_exception(backoff.expo, Exception, max_tries=3)
    def create_message(self, system_prompt, messages, max_tokens=1000, temperature=1.0):
        try:
            gpt_messages = [
                {"role": "system", "content": system_prompt}
            ] + messages

            completion = self.client.chat.completions.create(
                model="gpt-4o",
                max_tokens=max_tokens,
                messages=gpt_messages
            )

            return completion.choices[0].message.content
        except Exception as e:
            print(f"Error occurred: {e}, retrying...")
            raise e


class LLMSemanticChunker(BaseChunker):
    def __init__(self, organisation="openai", api_key=None, model_name="gpt-4o"):
        # import os
        # from openai import OpenAI

        # OPENAI_API_KEY = os.getenv('OPENAI_CHROMA_API_KEY')

        self.client = OpenAIClient(api_key=api_key, model_name=model_name)
        # self.client = AnthropicClient(api_key=os.getenv('ANTHROPIC_CHROMA_API_KEY')) # Will update

        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=50,
            chunk_overlap=0,
            length_function=openai_token_count
            )

    def get_prompt(self, chunked_input, current_chunk=0, invalid_response=None):
        messages = [
            {
                "role": "system", 
                "content": (
                    "You are an assistant specialized in splitting text into thematically consistent sections. "
                    "The text has been divided into chunks, each marked with <|start_chunk_X|> and <|end_chunk_X|> tags, where X is the chunk number. "
                    "Your task is to identify the points where splits should occur, such that consecutive chunks of similar themes stay together. "
                    "Respond with a list of chunk IDs where you believe a split should be made. For example, if chunks 1 and 2 belong together but chunk 3 starts a new topic, you would suggest a split after chunk 2. THE CHUNKS MUST BE IN ASCENDING ORDER."
                    "Your response should be in the form: 'split_after: 3, 5'."
                )
            },
            {
                "role": "user", 
                "content": (
                    "CHUNKED_TEXT: " + chunked_input + "\n\n"
                    "Respond only with the IDs of the chunks where you believe a split should occur. YOU MUST RESPOND WITH AT LEAST ONE SPLIT. THESE SPLITS MUST BE IN ASCENDING ORDER AND EQUAL OR LARGER THAN: " + str(current_chunk)+"." + (f"\n\The previous response of {invalid_response} was invalid. DO NOT REPEAT THIS ARRAY OF NUMBERS. Please try again." if invalid_response else "")
                )
            },
        ]
        return messages

    def split_text(self, text):
        import re

        chunks = self.splitter.split_text(text)

        split_indices = []

        # if "Good evening. Good evening. If I were smart, I’d go home now." in text:
        #     split_indices = [1, 6, 16, 19, 28, 33, 40, 45, 49, 53, 59, 63, 69, 75, 82, 86, 95, 101, 104, 109, 113, 116, 123, 128, 134, 141, 144, 152, 160, 168, 174, 184, 185, 190, 197, 200, 209, 211, 217, 227, 233, 235, 242, 251, 257, 265, 271, 275, 277, 283, 289, 295, 299, 303, 307]
        # elif " = Valkyria Chronicles III =" in text:
        #     split_indices = [11, 17, 26, 32, 43, 51, 57, 65, 66, 76, 77, 79, 89, 92, 93, 99, 105, 110, 116, 122, 130, 133, 141, 146, 150, 141, 146, 150, 154, 161, 163, 168, 172, 179, 186, 191, 197, 201, 205, 211, 217, 224, 228, 232, 237, 244, 251, 260, 268, 272, 274, 275, 281, 282, 288, 289, 299, 304, 315, 320, 321, 325, 329, 332, 336, 342, 344, 350, 358, 366, 376, 380, 388, 393, 402, 409, 414, 420, 425, 431, 436, 442, 444, 450, 458, 459, 469, 475, 478, 481, 483, 488, 494, 495, 501, 506, 512, 522, 530, 537, 547, 552, 559, 563, 569, 576, 580, 590, 596, 601, 615, 618, 624, 628, 635, 638, 644, 648, 651, 661]
        # elif "as of december 31, 2017, the company had gross state income tax credit carry-forwards of approximately $20 million, which expire from 2018 through 2020. a deferred tax asset of approximately $16 million (net of federal benefit) has been established related to these state income tax credit carry-forwards, with a valuation allowance of $7 million against such deferred tax asset as of december 31, 2017. the company h" in text:
        #     split_indices = [3, 5, 11, 19, 26, 29, 33, 38, 43, 47, 56, 57, 62, 66, 71, 75, 78, 84, 88, 89, 96, 97, 107, 116, 121, 132, 134, 137, 140, 146, 153, 155, 163, 166, 169, 175, 179, 185, 188, 192, 196, 198, 201, 204, 214, 220, 227, 228, 230, 234, 240, 241, 244, 247, 250, 257, 259, 265, 268, 274, 282, 286, 290, 294, 295, 300, 304, 314, 317, 321, 326, 329, 339, 343, 347, 355, 357, 362, 367, 371, 372, 375, 379, 385, 393, 394, 397, 401, 404, 410, 412, 414, 417, 423, 424, 431, 436, 438, 441, 446, 449, 454, 459, 464, 465, 469, 479, 482, 484, 486, 491, 498, 501, 502, 508, 516, 519, 520, 523, 525, 527, 530, 535, 540, 542, 550, 553, 557, 561, 567, 570, 579, 580, 589, 595, 598, 605, 609, 615, 622, 625, 626, 628, 632, 638, 639, 643, 653, 654, 665, 666, 669, 678, 681, 684, 695, 696, 699, 704, 712, 713, 720, 727, 730, 733, 740, 741, 745, 754, 756, 761, 764, 769, 771, 775, 780, 783, 787, 790, 794, 798, 804, 810, 812, 821, 823, 825, 829, 835, 838, 844, 847, 855, 859, 864, 871, 878, 885, 888, 891, 896, 901, 907, 909, 915, 922, 925, 926, 929, 933, 939, 946, 947, 949, 955, 959, 967, 968, 975, 981, 991, 992, 1002, 1007, 1019, 1020, 1022, 1027, 1031, 1035, 1045, 1047, 1050, 1052, 1058, 1062, 1066, 1069, 1080, 1084, 1089, 1090, 1095, 1099, 1102, 1108, 1112, 1114, 1120, 1124, 1128, 1129, 1132, 1141, 1145, 1150, 1159, 1164, 1168, 1174, 1180, 1189, 1195, 1197, 1205, 1209, 1218, 1219, 1227, 1231, 1235, 1239, 1242, 1251, 1255, 1257, 1263, 1270, 1275, 1276, 1282, 1284, 1291, 1294, 1296, 1298, 1310, 1311, 1317, 1323, 1327, 1337, 1343, 1348, 1355, 1358, 1359, 1368, 1373, 1379, 1381, 1385, 1391, 1394, 1396, 1403, 1410, 1412, 1416, 1424, 1430, 1432, 1439, 1449, 1459, 1460, 1465, 1469, 1475, 1482, 1485, 1486, 1493, 1494, 1503, 1504, 1509, 1515, 1518, 1525, 1532, 1538, 1541, 1545, 1546, 1550, 1551, 1555, 1559, 1565, 1569, 1572, 1576, 1586, 1588, 1591, 1595, 1600, 1603, 1610, 1616, 1619, 1624, 1630, 1636, 1640, 1643, 1645, 1650, 1654, 1664, 1668, 1670, 1680, 1682, 1688, 1689, 1698, 1703, 1707, 1714, 1718, 1732, 1733, 1742, 1752, 1758, 1759, 1763, 1767, 1773, 1781, 1782, 1787, 1796, 1798, 1802, 1811, 1813, 1818, 1822, 1828, 1831, 1834, 1840, 1845, 1852, 1853, 1862, 1864, 1872, 1877, 1885, 1888, 1890, 1893, 1896, 1902, 1909, 1915, 1920, 1930, 1931, 1934, 1944, 1950, 1958, 1970, 1972, 1975, 1980, 1983, 1988, 1998, 1999, 2005, 2014, 2023, 2025, 2031, 2035, 2041, 2049, 2055, 2056, 2061, 2069, 2071, 2076, 2083, 2084, 2088, 2094, 2099, 2104, 2108, 2110, 2115, 2120, 2121, 2126, 2131, 2135, 2136, 2139, 2143, 2149, 2157, 2158, 2161, 2167, 2174, 2177, 2181, 2188, 2195, 2200, 2202, 2205, 2210, 2214, 2218, 2221, 2226, 2228, 2229, 2233, 2236, 2240, 2243, 2246, 2248, 2252, 2262, 2266, 2271, 2273, 2275, 2284, 2286, 2289, 2291, 2294, 2296, 2300, 2306, 2307, 2315, 2321, 2328, 2329, 2331, 2338, 2348, 2357, 2364, 2368, 2374, 2379, 2385, 2391, 2397, 2398, 2402, 2404, 2413, 2419, 2424, 2426, 2430, 2438, 2441, 2445, 2456, 2457, 2465, 2473, 2474, 2481, 2488, 2494, 2501, 2502, 2516, 2517, 2519, 2525, 2529, 2535, 2537, 2547, 2550, 2554, 2560, 2562, 2573, 2582, 2585, 2589, 2595, 2596, 2602, 2611, 2612, 2620, 2624, 2627, 2630, 2634, 2637, 2641, 2645, 2652, 2659, 2662, 2663, 2666, 2675, 2682, 2684, 2690, 2697, 2701, 2704, 2708, 2714, 2721, 2723, 2731, 2735, 2743, 2745, 2754, 2759, 2767, 2770, 2777, 2788, 2791, 2796, 2799, 2803, 2810, 2814, 2816, 2820, 2827, 2831, 2835, 2838, 2839, 2849, 2853, 2858, 2859, 2867, 2869, 2874, 2875, 2881, 2887, 2888, 2901, 2904, 2909, 2913, 2918, 2923, 2927, 2931, 2936, 2938, 2940, 2950, 2955, 2963, 2965, 2973, 2977, 2986, 2987, 2992, 2999, 3006, 3010, 3011, 3019, 3020, 3023, 3025, 3031, 3035, 3043, 3044, 3050, 3051, 3059, 3062, 3063, 3067, 3073, 3083, 3095, 3099, 3109, 3115, 3120, 3127, 3132, 3135, 3141, 3146, 3151, 3153, 3158, 3162, 3164, 3165, 3173, 3180, 3181, 3185, 3194, 3199, 3202, 3208, 3218, 3228, 3230, 3235, 3241, 3251, 3255, 3256, 3263, 3273, 3274, 3285, 3289, 3295, 3300, 3304, 3311, 3315, 3321, 3325, 3329, 3334, 3339, 3341, 3343, 3347, 3353, 3357, 3359, 3362, 3371, 3374, 3381, 3387, 3390, 3396, 3403, 3409, 3412, 3415, 3423, 3427, 3431, 3435, 3436, 3448, 3455, 3456, 3469, 3475, 3476, 3483, 3487, 3489, 3501, 3503, 3511, 3512, 3515, 3519, 3528, 3530, 3537, 3545, 3547, 3549, 3553, 3558, 3563, 3565, 3574, 3582, 3584, 3587, 3592, 3604, 3605, 3612, 3618, 3625, 3630, 3632, 3639, 3646, 3650, 3659, 3666, 3667, 3675, 3677, 3682, 3689, 3691, 3695, 3703, 3710, 3711, 3715, 3724, 3725, 3727, 3732, 3744, 3749, 3753, 3760, 3763, 3766, 3770, 3772, 3785, 3786, 3799, 3805, 3809, 3815, 3820, 3827, 3828]
        short_cut = len(split_indices) > 0

        print(len(chunks))

        current_chunk = 0

        while True and not short_cut:
            if current_chunk >= len(chunks) - 4:
                break

            token_count = 0

            chunked_input = ''

            for i in range(current_chunk, len(chunks)):
                token_count += openai_token_count(chunks[i])
                chunked_input += f"<|start_chunk_{i+1}|>{chunks[i]}<|end_chunk_{i+1}|>"
                if token_count > 800:
                    break

            messages = self.get_prompt(chunked_input, current_chunk)
            while True:
                result_string = self.client.create_message(messages[0]['content'], messages[1:], max_tokens=200, temperature=0.2)
                # Use regular expression to find all numbers in the string
                split_after_line = [line for line in result_string.split('\n') if 'split_after:' in line][0]
                numbers = re.findall(r'\d+', split_after_line)
                # Convert the found numbers to integers
                numbers = list(map(int, numbers))

                print(numbers)

                # Check if the numbers are in ascending order and are equal to or larger than current_chunk
                if not (numbers != sorted(numbers) or any(number < current_chunk for number in numbers)):
                    break
                else:
                    messages = self.get_prompt(chunked_input, current_chunk, numbers)
                    print("Response: ", result_string)
                    print("Invalid response. Please try again.")

            split_indices.extend(numbers)

            current_chunk = numbers[-1]

            if len(numbers) == 0:
                break

        print(split_indices)

        # if "Good evening. Good evening. If I were smart, I’d go home now." in text:
        #     split_indices = [2, 4, 8, 11, 18, 22, 24, 26, 30, 34, 41, 43, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 70, 72, 74, 77, 80, 87, 89, 92, 96, 109, 112, 114, 118, 128, 136, 138, 141, 148, 152, 159, 161, 163, 165, 169, 171, 174, 178, 182, 185, 186, 191, 194, 197, 200, 204, 207, 209, 218, 226, 228, 230, 235, 242, 247, 249, 251, 254, 256, 260, 262, 265, 269, 271, 273, 276, 278, 280, 284, 287, 289, 291, 294, 296, 298, 300, 302, 304, 306, 308]
        # elif " = Valkyria Chronicles III =" in text:
        #     split_indices = [2, 4, 7, 9, 12, 16, 18, 20, 22, 25, 27, 30, 34, 36, 38, 40, 42, 44, 50, 52, 54, 56, 60, 63, 67, 70, 72, 78, 89, 91, 94, 97, 100, 103, 106, 108, 110, 112, 116, 118, 121, 124, 126, 128, 131, 134, 137, 140, 142, 146, 152, 159, 161, 164, 168, 172, 176, 178, 180, 184, 186, 189, 192, 194, 196, 198, 200, 203, 206, 212, 214, 216, 219, 221, 223, 226, 228, 230, 231, 233, 236, 239, 242, 244, 246, 248, 251, 258, 266, 270, 272, 275, 279, 283, 288, 290, 292, 294, 297, 302, 304, 306, 308, 310, 312, 314, 317, 320, 321, 324, 326, 329, 331, 333, 335, 346, 349, 350, 352, 356, 358, 364, 366, 368, 370, 373, 376, 380, 384, 386, 388, 390, 392, 394, 397, 399, 401, 403, 405, 407, 408, 411, 414, 418, 422, 424, 427, 430, 433, 436, 438, 440, 442, 444, 446, 448, 450, 452, 454, 456, 457, 459, 461, 463, 466, 468, 470, 472, 474, 476, 478, 480, 482, 485, 489, 494, 496, 500, 505, 510, 512, 514, 516, 518, 520, 522, 524, 526, 528, 530, 532, 536, 540, 546, 552, 565, 567, 571, 575, 577, 579, 581, 584, 586, 588, 591, 595, 597, 598, 602, 608, 610, 613, 616, 619, 621, 628, 635, 638, 643, 648, 650, 653, 656, 659]

        chunks_to_split_after = [i - 1 for i in split_indices]

        docs = []
        current_chunk = ''
        for i, chunk in enumerate(chunks):
            current_chunk += chunk + ' '
            if i in chunks_to_split_after:
                docs.append(current_chunk.strip())
                current_chunk = ''
        if current_chunk:
            docs.append(current_chunk.strip())

        return docs