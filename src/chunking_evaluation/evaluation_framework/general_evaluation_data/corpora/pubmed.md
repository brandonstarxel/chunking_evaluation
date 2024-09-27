PMID: 12929205
Accession ID: PMC176545
License: CC BY
Last Updated: 2021-01-05 08:21:03
Retracted: no
Citation: PLoS Biol. 2003 Oct 18; 1(1):e5
==== Front
PLoS BiolPLoS BiolpbioplosbiolPLoS Biology1544-91731545-7885Public Library of Science San Francisco, USA 10.1371/journal.pbio.0000005Research ArticleGenetics/Genomics/Gene TherapyInfectious DiseasesMicrobiologyPlasmodiumThe Transcriptome of the Intraerythrocytic Developmental Cycle of Plasmodium falciparum
 P. falciparum IDC TranscriptomeBozdech Zbynek 
1
Llinás Manuel 
1
Pulliam Brian Lee 
1
Wong Edith D 
1
Zhu Jingchun 
2
DeRisi Joseph L joe@derisilab.ucsf.edu
1
1Department of Biochemistry and Biophysics, University of California, San FranciscoSan Francisco, CaliforniaUnited States of America2Department of Biological and Medical Informatics, University of California, San FranciscoSan Francisco, CaliforniaUnited States of America10 2003 18 8 2003 18 8 2003 1 1 e512 6 2003 25 7 2003 Copyright: ©2003 Bozdech et al.2003This is an open-access article distributed under the terms of the Creative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are properly credited.
Microarray Analysis: Genome-Scale Hypothesis Scanning 

Monitoring Malaria: Genomic Activity of the Parasite in Human Blood Cells 

Plasmodium falciparum is the causative agent of the most burdensome form of human malaria, affecting 200–300 million individuals per year worldwide. The recently sequenced genome of P. falciparum revealed over 5,400 genes, of which 60% encode proteins of unknown function. Insights into the biochemical function and regulation of these genes will provide the foundation for future drug and vaccine development efforts toward eradication of this disease. By analyzing the complete asexual intraerythrocytic developmental cycle (IDC) transcriptome of the HB3 strain of P. falciparum, we demonstrate that at least 60% of the genome is transcriptionally active during this stage. Our data demonstrate that this parasite has evolved an extremely specialized mode of transcriptional regulation that produces a continuous cascade of gene expression, beginning with genes corresponding to general cellular processes, such as protein synthesis, and ending with Plasmodium-specific functionalities, such as genes involved in erythrocyte invasion. The data reveal that genes contiguous along the chromosomes are rarely coregulated, while transcription from the plastid genome is highly coregulated and likely polycistronic. Comparative genomic hybridization between HB3 and the reference genome strain (3D7) was used to distinguish between genes not expressed during the IDC and genes not detected because of possible sequence variations. Genomic differences between these strains were found almost exclusively in the highly antigenic subtelomeric regions of chromosomes. The simple cascade of gene regulation that directs the asexual development of P. falciparum is unprecedented in eukaryotic biology. The transcriptome of the IDC resembles a “just-in-time” manufacturing process whereby induction of any given gene occurs once per cycle and only at a time when it is required. These data provide to our knowledge the first comprehensive view of the timing of transcription throughout the intraerythrocytic development of P. falciparum and provide a resource for the identification of new chemotherapeutic and vaccine candidates.

A tight cascade of gene regulation during the lifecycle of the malaria parasite in human blood cells suggests new functions for many Plasmodium genes
==== Body
Introduction
Human malaria is caused by four species of the parasitic protozoan genus Plasmodium. Of these four species, Plasmodium falciparum is responsible for the vast majority of the 300–500 million episodes of malaria worldwide and accounts for 0.7–2.7 million annual deaths. In many endemic countries, malaria is responsible for economic stagnation, lowering the annual economic growth in some regions by up to 1.5% (Sachs and Malaney 2002). While isolated efforts to curb malaria with combinations of vector control, education, and drugs have proven successful, a global solution has not been reached. Currently, there are few antimalarial chemotherapeutics available that serve as both prophylaxis and treatment. Compounding this paucity of drugs is a worldwide increase in P. falciparum strains resistant to the mainstays of antimalarial treatment (Ridley 2002). In addition, the search for a malaria vaccine has thus far been unsuccessful. Given the genetic flexibility and the immunogenic complexity of P. falciparum, a comprehensive understanding of Plasmodium molecular biology will be essential for the development of new chemotherapeutic and vaccine strategies.

The 22.8 Mb genome of P. falciparum is comprised of 14 linear chromosomes, a circular plastid-like genome, and a linear mitochondrial genome. The malaria genome sequencing consortium estimates that more than 60% of the 5,409 predicted open reading frames (ORFs) lack sequence similarity to genes from any other known organism (Gardner et al. 2002). Although ascribing putative roles for these ORFs in the absence of sequence similarity remains challenging, their unique nature may be key to identifying Plasmodium-specific pathways as candidates for antimalarial strategies.

The complete P. falciparum lifecycle encompasses three major developmental stages: the mosquito, liver, and blood stages. It has long been a goal to understand the regulation of gene expression throughout each developmental stage. Previous attempts to apply functional genomics methods to address these questions used various approaches, including DNA microarrays (Hayward et al. 2000; Ben Mamoun et al. 2001; Le Roch et al. 2002), serial analysis of gene expression (Patankar et al. 2001), and mass spectrometry (Florens et al. 2002; Lasonder et al. 2002) on a limited number of samples from different developmental stages. While all of these approaches have provided insight into the biology of this organism, there have been no comprehensive analyses of any single developmental stage. Here we present an examination of the full transcriptome of one of these stages, the asexual intraerythrocytic developmental cycle (IDC), at a 1-h timescale resolution.

The 48-h P. falciparum IDC (Figure 1A) initiates with merozoite invasion of red blood cells (RBCs) and is followed by the formation of the parasitophorous vacuole (PV) during the ring stage. The parasite then enters a highly metabolic maturation phase, the trophozoite stage, prior to parasite replication. In the schizont stage, the cell prepares for reinvasion of new RBCs by replicating and dividing to form up to 32 new merozoites. The IDC represents all of the stages in the development of P. falciparum responsible for the symptoms of malaria and is also the target for the vast majority of antimalarial drugs and vaccine strategies.

Figure 1 Parasite Culturing and Data Characteristics of the P. falciparum IDC Transcriptome Analysis
(A) Giemsa stains of the major morphological stages throughout the IDC are shown with the percent representation of ring-, trophozoite-, or schizont-stage parasites at every timepoint. The 2-h invasion window during the initiation of the bioreactor culture is indicated (gray area).

(B–D) Example expression profiles for three genes, encoding EBA175, DHFR-TS, and ASL, are shown with a loess fit of the data (red line).

(E) MAL6P1.147, the largest predicted ORF in the Plasmodium genome, is represented by 14 unique DNA oligonucleotide elements. The location of each of the oligonucleotide elements within the predicted ORF and the corresponding individual expression profiles are indicated (oligo 1–14). A red/green colorimetric representation of the gene expression ratios for each oligonucleotide is shown below the graph. The pairwise Pearson correlation for these expression profiles is 0.98 ± 0.02.

(F) The percentage of the power in the maximum frequency of the FFT power spectrum was used as an indicator of periodicity. A histogram of these values reveals a strong bias toward single-frequency expression profiles, indicating that the majority of P. falciparum genes are regulated in a simple periodic manner. This bias is eliminated when the percent power was recalculated using random permutations of the same dataset (inset). For reference, the locations of EBA175 (peak B), DHFR-TS (peak C), and ASL (peak D) are shown.

Our laboratory has developed a P. falciparum–specific DNA microarray using long (70 nt) oligonucleotides as representative elements for predicted ORFs in the sequenced genome (strain 3D7) (Bozdech et al. 2003). Using this DNA microarray, we have examined expression profiles across 48 individual 1-h timepoints from the IDC of P. falciparum. Our data suggest that not only does P. falciparum express the vast majority of its genes during this lifecycle stage, but also that greater than 75% of these genes are activated only once during the IDC. For genes of known function, we note that this activation correlates well with the timing for the respective protein's biological function, thus illustrating an intimate relationship between transcriptional regulation and the developmental progression of this highly specialized parasitic organism. We also demonstrate the potential of this analysis to elucidate the function of the many unknown gene products as well as for further understanding the general biology of this parasitic organism.

Results
Expression Profiling of the IDC
The genome-wide transcriptome of the P. falciparum IDC was generated by measuring relative mRNA abundance levels in samples collected from a highly synchronized in vitro culture of parasites. The strain used was the well-characterized Honduran chloroquine-sensitive HB3 strain, which was used in the only two experimental crosses carried out thus far with P. falciparum (Walliker et al. 1987; Wellems et al. 1990). To obtain sufficient quantities of parasitized RBCs and to ensure the homogeneity of the samples, a large-scale culturing technique was developed using a 4.5 l bioreactor (see Materials and Methods). Samples were collected for a 48-h period beginning 1 h postinvasion (hpi). Culture synchronization was monitored every hour by Giemsa staining. We observed only the asexual form of the parasite in these stains. The culture was synchronous, with greater than 80% of the parasites invading fresh RBCs within 2 h prior to the harvesting of the first timepoint. Maintenance of synchrony throughout the IDC was demonstrated by sharp transitions between the ring-to-trophozoite and trophozoite-to-schizont stages at the 17- and 29-h timepoints, respectively (Figure 1A).

The DNA microarray used in this study consists of 7,462 individual 70mer oligonucleotides representing 4,488 of the 5,409 ORFs manually annotated by the malaria genome sequencing consortium (Bozdech et al. 2003). Of the 4,488 ORFs, 990 are represented by more than one oligonucleotide. Since our oligonucleotide design was based on partially assembled sequences periodically released by the sequencing consortium over the past several years, our set includes additional features representing 1,315 putative ORFs not part of the manually annotated collection. In this group, 394 oligonucleotides are no longer represented in the current assembled sequence. These latter ORFs likely fall into the gaps present in the published assembly available through the Plasmodium genome resource PlasmoDB.org (Gardner et al. 2002; Kissinger et al. 2002; Bahl et al. 2003).

To measure the relative abundance of mRNAs throughout the IDC, total RNA from each timepoint was compared to an arbitrary reference pool of total RNA from all timepoints in a standard two-color competitive hybridization (Eisen and Brown 1999). The transcriptional profile of each ORF is represented by the mean-centered series of ratio measurements for the corresponding oligonucleotide(s) (Figure 1B–1E). Inspection of the entire dataset revealed a striking nonstochastic periodicity in the majority of expression profiles. The relative abundance of these mRNAs continuously varies throughout the IDC and is marked by a single maximum and a single minimum, as observed for the representative schizont-specific gene, erythrocyte-binding antigen 175 (eba175), and the trophozoite-specific gene, dihydrofolate reductase–thymidylate synthetase (dhfr-ts) (Figure 1B and 1C). However, there is diversity in both the absolute magnitude of relative expression and in the timing of maximal expression (phase). In addition, a minority of genes, such as adenylosuccinate lyase (asl) (Figure 1D), displayed a relatively constant expression profile. The accuracy of measurements from individual oligonucleotides was further verified by the ORFs that are represented by more than one oligonucleotide feature on the microarray. The calculated average pairwise Pearson correlation (r) is greater than 0.90 for 68% (0.75 for 86%) of the transcripts represented by multiple oligonucleotides with detectable expression during the IDC (Table S1). Cases in which data from multiple oligonucleotides representing a single putative ORF disagree may represent incorrect annotation. The internal consistency of expression profile measurements for ORFs represented by more than one oligonucleotide sequence is graphically shown in Figure 1E for the hypothetical protein MAL6P1.147, the largest predicted ORF in the genome (31 kb), which is represented by 14 oligonucleotide elements spanning the entire length of the coding sequence. The average pairwise correlation (r) for these features is 0.98±0.02.

Periodicity in genome-wide gene expression datasets has been used to identify cell-cycle-regulated genes in both yeast and human cells (Spellman et al. 1998; Whitfield et al. 2002). Owing to the cyclical nature of the P. falciparum IDC dataset, a similar computational approach was taken. We performed simple Fourier analysis, which allowed us to calculate both the apparent phase and frequency of expression for each gene during the IDC (see Materials and Methods). The fast Fourier transform (FFT) maps a function in a time domain (the expression profile) into a frequency domain such that when the mapped function is plotted (the power spectra), sharp peaks appear at frequencies where there is intrinsic periodicity. The calculated power spectra for each expression profile confirmed the observation that the data are highly periodic. The majority of profiles exhibited an overall expression period of 0.75–1.5 cycles per 48 h.

We have used the FFT data for the purpose of filtering the expression profiles that are inherently noisy (i.e., that have low signal) or that lack differential expression throughout the IDC. Since the majority of the profiles display a single low-frequency peak in the power spectrum, we have taken advantage of this feature to classify profiles, similar to the application of a low-pass filter in signal processing. By measuring the power present in the peak frequency window (the main component plus two adjacent peaks) relative to the power present at all frequencies of the power spectrum, we were able to define a score (percent power) that we have used to stratify the dataset. The resulting distribution of expression profiles, scored in this way, is shown in Figure 1F for all oligonucleotides. For reference, the positions of profiles corresponding to eba175 (peak B), dhfr-ts (peak C), and asl (peak D) are indicated. It is striking that 79.5% of the expression profiles have a very high score (greater than 70%). For comparison, we applied our FFT analysis to the Saccharomyces cerevisiae cell cycle data, yielding only 194 profiles (3.8%) above a 70% score (Figure S1). In addition, we randomly permuted the columns of the complete dataset 1,000 times, each time recalculating the FFT, for a total of 5 million profiles (see inset in Figure 1F). The randomized set exhibits essentially no periodicity: the probability of any random profile scoring above 70% is 1.3 × 10−5.


P. falciparum Transcriptome Overview
To provide an overview of the IDC transcriptome, we selected all 3,719 microarray elements whose profiles exhibited greater than 70% of the power in the maximum frequency window and that were also in the top 75% of the maximum frequency magnitudes. Although hierarchical clustering is extremely useful for comparing any set of expression data, regardless of the experimental variables, we sought to specifically address temporal order within the dataset. To accomplish this, the FFT phase was used to order the expression profiles to create a phaseogram of the IDC transcriptome of P. falciparum (Figure 2A). The overview set represents 2,714 unique ORFs (3,395 oligonucleotides). An additional 324 oligonucleotides represent ORFs that are not currently part of the manually annotated collection.

Figure 2 Overview of the P. falciparum IDC Transcriptome
(A) A phaseogram of the IDC transcriptome was created by ordering the transcriptional profiles for 2,712 genes by phase of expression along the y-axis. The characteristic stages of intraerythrocytic parasite morphology are shown on the left, aligned with the corresponding phase of peak gene expression.

(B–M) The temporal ordering of biochemical processes and functions is shown on the right. Each graph corresponds to the average expression profile for the genes in each set and the mean peak-to-trough amplitude is shown in parentheses.

The IDC phaseogram depicts a cascade of continuous expression lacking clear boundaries or sharp transitions. During the first half of the IDC, a large number of genes involved in general eukaryotic cellular functions are induced with broad expression profiles. This gradual continuum includes the transition from the ring to the early trophozoite stage and the trophozoite to the early schizont stage, encompassing approximately 950 and 1,050 genes, respectively. Next, the mid- and late-schizont stages are marked by a rapid, large amplitude induction of approximately 550 genes, many of which appear to be continually expressed into the early-ring stage. However, owing to the level of synchrony in the culture, the ring-stage signal may be partially attributed to cross-contamination from residual schizonts. In the final hours of the IDC, approximately 300 genes corresponding to the early-ring stage are induced, indicating that reinvasion occurs without obvious interruptions to initiate the next cycle. The expression profiles for developmentally regulated genes in the P. falciparum IDC transcriptome reveal an orderly timing of key cellular functions. As indicated in Figure 2B–2M, groups of functionally related genes share common expression profiles and demonstrate a programmed cascade of cellular processes that ensure the completion of the P. falciparum IDC.

Ring and Early-Trophozoite Stage
In the following text, we have grouped the genes according to temporal expression phases based on their association with the common P. falciparum cytological stages.

Following invasion, approximately 950 ORFs are induced during the ring and early trophozoite stage, including genes associated with the cytoplasmic transcriptional and translational machinery, glycolysis and ribonucleotide biosynthesis (Figure 2B–2E). Represented in this group are 23 ORFs involved in transcription, including the four subunits of RNA polymerase I, nine subunits of RNA polymerase II, three subunits of RNA polymerase III, and four transcription factors. The average expression profile for this group is shown in Figure 2B. (See Table S2 for all functional group details.) Also in this set are three previously identified P. falciparum RNA polymerase genes: the large subunits of P. falciparum RNA polymerase I (Fox et al. 1993) and RNA polymerase II (Li et al. 1989) and RNA polymerase III (Li et al. 1991). The cytoplasmic translation gene group (Figure 2C) consists of 135 ORFs including homologues for 34 small and 40 large ribosomal subunits, 15 translation initiation factors, five translation elongation factors, 18 aminoacyl-tRNA synthetases, and 23 RNA helicases. In addition to the manually annotated ORFs, the translation gene group contains three ORFs predicted only by automated annotation including two ribosomal proteins (chr5.glm_215, chr5.glm_185) and a homologue of eIF-1A (chr11.glm_489) (PlasmoDB.org). In one case, chr5.glm_185 overlaps with the manually annotated ORF PFE0850w, which is found on the opposite strand. Oligonucleotide elements for both of these ORFs are present on the array. The oligonucleotide corresponding to the automated prediction yielded a robust FFT score and a phase consistent with the translation machinery, yet no PFE0850w expression was detected. These results suggest that the automated prediction for chr5.glm_185 most likely represents the correct gene model for this genomic locus and illustrates the use of the IDC expression data for further verification of the P. falciparum genome annotations.

Another set of 33 ORFs with homology to components of the translational machinery displayed an entirely distinct expression pattern, being induced during the late-trophozoite and early-schizont stage. This group includes 11 homologues of chloroplast ribosomal proteins, four mitochondrial/chloroplast elongation factors, and six amino acid tRNA synthetases (Table S2). These ORFs also share a common pattern of expression, suggesting that these factors are components of the mitochondrial and/or the plastid translation machinery. This observation is supported by the presence of predicted apicoplast-targeting signals in 18 of these proteins (PlasmoDB.org). In addition, one of these factors, ribosomal protein S9, has been experimentally immunolocalized within the plastid (Waller et al. 1998). These data suggest that the peak of expression for the cytoplasmic translation machinery occurs in the first half of the IDC, whereas plastid and mitochondrial protein synthesis is synchronized with the maturation of these organelles during the second half of the IDC.

In addition to transcription and translation, genes involved in several basic metabolic pathways were also induced during the ring and early-trophozoite stage, including glycolysis and ribonucleotide biosynthesis (Figure 2D and 2E). Unlike the majority of  P. falciparum biochemical processes, most of the enzymes involved in nucleotide metabolism and glycolysis have been identified (Reyes et al. 1982; Sherman 1998). The glycolysis group (Figure 2D) is tightly coregulated throughout the IDC and contains all of the 12 known enzymes. Expression initiates after reinvasion and continues to increase toward maximal expression during the trophozoite stage, when metabolism is at its peak. The glycolytic pathway is very well preserved in P. falciparum and exemplifies how data from this study can complement the homology-based interpretation of the genome. First, the genome contains two putative copies of pyruvate kinase on chromosomes 6 and 10, MAL6P1.160 and PF10_0363, respectively (Gardner et al. 2002). However, only one of these genes, MAL6P1.160, has a similar expression profile to the other known glycolytic enzymes, suggesting that this enzyme is the main factor of this step in the glycolytic pathway. Interestingly, PF10_0363 contains a putative apicoplast-targeting signal (PlasmoDB.org). In another case, the malaria genome sequencing consortium has predicted two homologues of triose phosphate isomerase, PF14_0378 and PFC0381w. The latter is not detected by our analysis, suggesting that this gene is utilized in another developmental stage or may be a nonfunctional, redundant homologue.


P. falciparum parasites generate pyrimidines through a de novo synthesis pathway while purines must be acquired by the organism through a salvage pathway (Gero and O'Sullivan 1990). The mRNA levels of 16 enzymes corresponding to members of the pyrimidine ribonucleotide synthesis pathway, beginning with carbamoyl phosphate synthetase and ending with CTP synthetase, were uniformly induced immediately after invasion (Figure 2E). The relative abundance of these transcripts peaked at approximately 18–22 hpi and then rapidly declined. Similar expression characteristics were detected for the enzymes of the purine salvage pathway, including the nucleoside conversion enzymes, hypoxanthine–guanine–xanthine phosphoribosyltransferase, and both guanylate and adenylate kinases (Figure 2E; Table S2).

Trophozoite and Early-Schizont Stage
The mRNA expression data indicate that ribonucleotide and deoxyribonucleotide production is clearly bifurcated into two distinct temporal classes. While ribonucleotide synthesis is required in the early stages of the IDC, deoxyribonucleotide metabolism is a trophozoite/early-schizont function. mRNA transcripts for enzymes that convert ribonucleotides into deoxyribonucleotides, including DHFR-TS and both subunits of ribonucleotide reductase, were induced approximately at 10 hpi, peaking at approximately 32 hpi (Figure 2F). This represents a temporal shift from the induction of ribonucleotide synthesis of approximately 8–10 h. The expression of the deoxyribonucleotide biosynthesis is concomitant with the induction of DNA replication machinery transcripts, reflecting a tight relationship between DNA synthesis and production of precursors for this process.

Thirty-two ORFs with homologies to various eukaryotic DNA replication machinery components are transcribed during the late-trophozoite and early-schizont stage. The timing of their transcription presages cell division. This functional gene group (Figure 2G), with peak expression around 32 hpi, contains the previously characterized P. falciparum DNA Polα, DNA Polδ, and proliferating cell nuclear antigen, as well as the vast majority of the DNA replication components predicted by the malaria genome sequencing consortium (Gardner et al. 2002). These additional components include eight predicted DNA polymerase subunits, two putative origin recognition complex subunits, six minichromosome maintenance proteins, seven endo- and exonucleases, seven replication factor subunits, and two topoiosomerases. Interestingly, a number of proteins typically required for eukaryotic DNA replication, including the majority of the subunits of the origin recognition complex, have not yet been identified by conventional sequence similarity searches of the P. falciparum genome.

All genes necessary for the completion of the tricarboxylic acid (TCA) cycle were detected in the Plasmodium genome (Gardner et al. 2002), although earlier studies indicate an unconventional function for this metabolic cycle. These studies suggest that the TCA cycle does not play a major role in the oxidation of glycolytic products. Instead, it is essential for the production of several metabolic intermediates, such as succinyl-CoA, a precursor of porphyrin biosynthesis (Sherman 1998). The peak of expression for all TCA factors was detected during the late-trophozoite and early-schizont stage (Figure 2H). Consistent with the model suggesting a disconnection of the TCA cycle from glycolysis during the IDC, no expression was detected for the subunits of the pyruvate dehydrogenase complex, including the α and β chains of pyruvate dehydrogenase and dihydrolipoamide S-acetyl transferase, the typical links between glycolysis and the TCA cycle. On the other hand, expression of TCA cycle genes is well synchronized with the expression of a large number of mitochondrial genes, including the three ORFs of the mitochondrial genome (Feagin et al. 1991), and several factors of electron transport (Table S2). Although some of the TCA cycle proteins have been localized to the cytoplasm (Lang-Unnasch 1992), the expression data suggest an association of this biochemical process with mitochondrial development and possibly with the abbreviated electron transport pathway detected in this organelle.

Schizont Stage
A transition from early to mid-schizont is marked by the maximal induction of 29 ORFs predicted to encode various subunits of the proteasome (Figure 2I). Seven α and six β subunits of the 20S particle and 16 ORFs of the 19S regulatory particle were identified in this gene group. The common expression profile for the subunits of both of the 26S particle complexes suggests the involvement of ubiquitin-dependent protein degradation in the developmental progression of the parasite. The peak of proteasome expression coincides with a transition in the IDC transcriptome from metabolic and generic cellular machinery to specialized parasitic functions in the mid-schizont stage. This suggests an association between transcriptional regulation and protein turnover during this and possibly other transitions during the progression of the P. falciparum IDC.

In the schizont stage, one of the first specialized processes induced was expression from the plastid genome (Figure 2J). The essential extrachromosomal plastid (or apicoplast) genome contains 60 potentially expressed sequences, including ribosomal proteins, RNA polymerase subunits, ribosomal RNAs, tRNAs, and nine putative ORFs, including a ClpC homologue (Wilson et al. 1996). Very little is known about the regulation of gene expression in the plastid, but it is thought to be polycistronic (Wilson et al. 1996). In support of this observation, we find that 27 of the 41 plastid-specific elements present on our microarray displayed an identical expression pattern (Figure 3C). The remaining elements correspond mainly to tRNAs and failed to detect appreciable signal. The highly coordinated expression of the plastid genome, whose gene products are maximally expressed in the late-schizont stage, is concomitant with the replicative stage of the plastid (Williamson et al. 2002). Note that not all plastid ORFs are represented on the microarray used in this study, and thus it is a formal possibility that the expression of the missing genes may differ from those shown in Figure 3C.

Figure 3 Coregulation of Gene Expression along the Chromosomes of P. falciparum Is Rare, While Plastid Gene Expression Is Highly Coordinated
Expression profiles for oligonucleotides are shown as a function of location for Chromosome 2 ([A], Oligo Map). With the exception of the SERA locus (B), coregulated clusters of adjacent ORFs are seldom observed, indicating that expression phase is largely independent of chromosomal position. (C) In contrast to the nuclear chromosomes, the polycistronic expression of the circular plastid genome is reflected in the tight coregulation of gene expression. This is an expanded view of the plastid-encoded genes from Figure 2J. Genomic differences between strain 3D7, from which the complete genome was sequenced, and strain HB3 were measured by CGH. The relative hybridization between the gDNA derived from these two strains is shown as a percent reduction of the signal intensity for 3D7 ([A], CGH Data). Differences between the two strains are predominately located in the subtelomeric regions that contain the highly polymorphic var, rifin, and stevor gene families. Intrachromosomal variations, as observed for the msp2 gene, were rare.

Offset from the plastid by approximately 6 h, a set of approximately 500 ORFs exhibited peak expression during the late-schizont stage. Merozoite invasion of a new host cell is a complex process during which the parasite must recognize and dock onto the surface of the target erythrocyte, reorient with its apical tip toward the host cell, and internalize itself through invagination of the erythrocytic plasma membrane. The entire sequence of invasion events is facilitated by multiple receptor–ligand interactions with highly specialized plasmodial antigens (Cowman et al. 2000). The merozoite invasion group contains 58 ORFs, including 26 ORFs encoding antigens previously demonstrated to be important for the invasion process (see Figure 2K). These include integral membrane proteins delivered to the merozoite surface from the micronemes (AMA1 and EBA175), GPI-anchored proteins of the merozoite membrane (MSP1, MSP4, and MSP5), proteins extrinsically associated with the merozoite surface during their maturation in the PV (MSP3 and MSP6), and soluble proteins secreted to the parasite–host cell interface (RAP1, RAP2, and RAP3). In addition, late-schizont-specific expression was observed for several antigens whose functions are not completely understood, but which have been associated with the invasion process. These ORFs include the merozoite-capping protein (MCP1), erythrocyte-binding-like protein 1 (EBL1), reticulocyte-binding proteins (RBP1 and RBP2), acid basic repeat antigen (ABRA), MSP7, and a homologue of the Plasmodium yoelii merozoite antigen 1. As expected, peak expression of these antigens coincides with the maturation of merozoites and development of several apical organelles, including rhoptries, micronemes, and dense granules. Many of these proteins have been considered as vaccine candidates since antibodies against these antigens were readily detected in the immune sera of both convalescent patients as well as individuals with naturally acquired immunity (Preiser et al. 2000).

The sensitivity of invasion to protease and kinase inhibitors indicates an essential role for these activities in merozoite release as well as in the reinvasion process (Dluzewski and Garcia 1996; Blackman 2000; Greenbaum et al. 2002). The merozoite invasion gene group contains three serine proteases, including PfSUB1, PfSUB2, and an additional homologue to plasmodial subtilases (PFE0355c), and two aspartyl proteases, plasmepsin (PM) IX and X. Peak expression during the mid-schizont stage was also observed for seven members of the serine repeat antigen (SERA) family, all of which contain putative cysteine protease domains. In addition to the proteases, expression of 12 serine/threonine protein kinases and three phophorylases was tightly synchronized with the genes of the invasion pathway, including six homologues of protein kinase C, three Ca+-dependent and two cAMP-dependent kinases, phosphatases 2A and 2B, and protein phosphatase J.

Another functionally related gene group whose expression is sharply induced during the late-schizont stage includes components of actin–myosin motors (see Figure 2L) (Pinder et al. 2000). As in other apicomplexa, actin and myosin have been implicated in host cell invasion (Opitz and Soldati 2002). Schizont-specific expression was observed for three previously described class XIV myosin genes, one associated light chain, two actin homologues, and three additional actin cytoskeletal proteins, including actin-depolymerizing factor/cofilin (two isoforms) and coronin (one isoform). Although the molecular details of plasmodial actin–myosin invasion are not completely understood, the tight transcriptional coregulation of the identified factors indicates that the examination of schizont-specific expression may help to identify additional, possibly unique elements of this pathway.

Early-Ring Stage
The expression data are continuous throughout the invasion process, with no observable abrupt change in the expression program upon successful reinvasion. However, a set of approximately 300 ORFs whose expression is initiated in the late-schizont stage persists throughout the invasion process and peaks during the early-ring stages (see Figure 2M). It was previously determined that immediately after invasion, a second round of exocytosis is triggered, ensuring successful establishment of the parasite within the host cell (Foley et al. 1991). One of the main P. falciparum virulence factors associated with this process is ring-infected surface antigen 1 (RESA1). RESA1 is secreted into the host cell cytoplasm at the final stages of the invasion process, where it binds to erythrocytic spectrin, possibly via its DnaJ-like chaperone domain (Foley et al. 1991). The early stages of the IDC contain a variety of putative molecular chaperones in addition to RESA1, including RESA2 and RESAH3, plus five additional proteins carrying DnaJ-like domains. However, the functional roles of these chaperones remain unclear. Despite the cytoplasmic role of RESA1, abundant antibodies specific for RESA1 are present in individuals infected with P. falciparum, indicating that RESA1 is also presented to the host immune system (Troye-Blomberg et al. 1989). Several genes encoding additional antigenic factors are found among the early ring gene group, including frequently interspersed repeat antigen (FIRA), octapeptide antigen, MSP8, and sporozoite threonine- and asparagine-rich protein (STARP). Like RESA1, antibodies against these antigens are also found in the sera of infected individuals, suggesting that the final stages of invasion might be a target of the immune response.

Overall, the genes expressed during the mid- to late-schizont and early-ring stage encode proteins predominantly involved in highly parasite-specific functions facilitating various steps of host cell invasion. The expression profiles of these genes are unique in the IDC because of the large amplitudes and narrow peak widths observed. The sharp induction of a number of parasite-specific functions implies that they are crucial for parasite survival in the mammalian host and hence should serve as excellent targets for both chemotherapeutic and vaccine-based antimalarial strategies.

IDC Transcriptional Regulation and Chromosomal Structure
Transcriptional regulation of chromosomal gene expression in P. falciparum is thought to be monocistronic, with transcriptional control of gene expression occurring through regulatory sequence elements upstream and downstream of the coding sequence (Horrocks et al. 1998). This is in contrast to several other parasites, such as Leishmania sp., in which polycistronic mRNA is synthesized from large arrays of coding sequences positioned unidirectionally along the arms of relatively short chromosomes (Myler et al. 2001). Recent proteomic analyses failed to detect any continuous chromosomal regions with common stage-specific gene expression in several stages of the P. falciparum lifecycle (Florens et al. 2002). However, transcriptional domains have previously been suggested for Chromosome 2 (Le Roch et al. 2002). The availability of the complete P. falciparum genome coupled with the IDC transcriptome allows us to investigate the possibility of chromosomal clustering of gene expression (see Figure 3A). To systematically explore the possibility of coregulated expression as a function of chromosomal location, we applied a Pearson correlation to identify similarities in expression profiles among adjacent ORFs. The pairwise Pearson correlation was calculated for every ORF pair within each chromosome (Figure S2). Gene groups in which the correlation of 70% of the possible pairs was greater than r = 0.75 were classified as putative transcriptionally coregulated groups. Using these criteria, we identified only 14 coregulation groups consisting of greater than three genes, with the total number of genes being 60 (1.4% of all represented genes) (Table S3). In eight of the 14 groups, the coregulation of a pair of genes may be explained by the fact that they are divergently transcribed from the same promoter. A set of 1,000 randomized permutations of the dataset yielded 2.25 gene groups. Contrary to the nuclear chromosomes, there was a high correlation of gene expression along the plastid DNA element, consistent with polycistronic transcription (see Figure 3C). The average pairwise Pearson correlation for a sliding window of seven ORFs along the plastid genome is 0.92±0.03.

The largest group demonstrating coregulation on the nuclear chromosomes corresponds to seven genes of the SERA family found on Chromosome 2 (see Figure 3B) (Miller et al. 2002). Besides the SERA gene cluster and a group containing three ribosomal protein genes, no additional functional relationship was found among the other chromosomally adjacent, transcriptionally coregulated gene groups. The limited grouping of regional chromosomal expression was independent of strand specificity and, with the exception of the SERA group, did not overlap with the groups of “recently duplicated genes” proposed by the malaria genome sequencing consortium (Gardner et al. 2002).

Three major surface antigens, the var, rifin, and stevor families, have a high degree of genomic variability and are highly polymorphic between strains and even within a single strain (Cheng et al. 1998; Afonso Nogueira et al. 2002; Gardner et al. 2002). Expression profiles for only a small subset of these genes were detected in the IDC transcriptome and were typically characterized by low-amplitude profiles. This could be due to two nonmutually exclusive possibilities: first, the HB3 DNA sequence for these genes may be substantially rearranged or completely deleted relative to the reference strain, 3D7; second, only a few of these genes may be selectively expressed, as has been proposed (Deitsch et al. 2001). To identify regions of genomic variability between 3D7 and HB3, we performed microarray-based comparative genomic hybridization (CGH) analysis. Array-based CGH has been performed with human cDNA and bacterial artificial chromosome-based microarrays to characterize DNA copy-number changes associated with tumorigenesis (Gray and Collins 2000; Pollack et al. 2002). Using a similar protocol, CGH analysis revealed that the majority of genetic variation between HB3 and 3D7 is confined to the subtelomeric chromosomal regions containing the aforementioned gene families (Figure 3A; Figure S3). Only 28.3% of rifin, 47.1% of var, and 51.0% of stevor genes predicted for the 3D7 strain were detected for the HB3 genomic DNA (gDNA) when hybridized to the 3D7-based microarray. Thus, the underrepresentation of these gene families in the HB3 IDC transcriptome is likely due to the high degree of sequence variation present in these genes. Excluding the three surface antigen families in the subtelomeric regions, 97% of the remaining oligonucleotide microarray elements exhibit an equivalent signal in the CGH analysis. However, 144 of the differences detected by CGH reside in internal chromosomal regions and include several previously identified plasmodial antigens: MSP1, MSP2 (Figure 3A), S antigen, EBL1, cytoadherence-linked asexual gene 3.1 (CLAG3.1), glutamine-rich protein (GLURP), erythrocyte membrane protein 3 (PfEMP3), knob-associated histidine-rich protein (KAHRP), and gametocyte-specific antigen Pfg377 (Table S4). These results demonstrate a high degree of genetic variation within the genes considered to be crucial for antigenic variation between these two commonly used laboratory strains of P. falciparum.

Implications for Drug Discovery
The majority of the nuclear-encoded proteins targeted to the plastid are of prokaryotic origin, making them excellent drug targets (McFadden and Roos 1999). Moreover, inhibitors of plastid-associated isoprenoid biosynthesis, DNA replication, and translation have been shown to kill the P. falciparum parasite, demonstrating that the plastid is an essential organelle (Fichera and Roos 1997; Jomaa et al. 1999). The plastid has been implicated in various metabolic functions, including fatty acid metabolism, heme biosynthesis, isoprenoid biosynthesis, and iron–sulfur cluster formation (Wilson 2002). It is clear that, within the plastid, functional ribosomes are assembled to express the ORFs encoded by the plastid genome (Roy et al. 1999). However, nuclear-encoded components are required to complete the translational machinery as well as for all other plastid metabolic functions. A bipartite signal sequence is required for efficient transport of these nuclear proteins from the cytoplasm to the plastid via the endoplasmic reticulum (Waller et al. 2000). Computational predictions suggest that the P. falciparum genome may contain over 550 nuclear-encoded proteins with putative transit peptides (Zuegge et al. 2001; Foth et al. 2003).

Given that over 10% of the ORFs in the P. falciparum genome are predicted to contain an apicoplast-targeting sequence, we sought to use the IDC transcriptome as a means to narrow the search space for candidate apicoplast-targeted genes. As mentioned above, the expression profiles for genes encoded on the plastid genome are tightly coordinated (see Figure 3C). We reasoned that genes targeted to the plastid would be expressed slightly before or coincidentally with the plastid genome. Therefore, we utilized the FFT phase information to identify ORFs in phase with expression of the plastid genome (see Materials and Methods) (Table S5). Because the genes of the plastid genome are maximally expressed between 33 and 36 hpi, we searched for all genes in the dataset with an FFT phase in this time window and then cross-referenced the list of predicted apicoplast-targeted sequences (PlasmoDB.org), resulting in a list of 124 in-phase apicoplast genes (Figure 4A). Within this list are two ORFs that have been directly visualized in the apicoplast, acyl carrier protein and the ribosomal subunit S9 (Waller et al. 1998), as well as many ORFs associated with the putative plastid ribosomal machinery, enzymes involved in the nonmevalonate pathway, additional caseineolytic proteases (Clps), the reductant ferredoxin, and replication/transcriptional machinery components. However, this list contains only 14 of the 43 proteins categorized in the Gene Ontology (GO) assignments at PlasmoDB.org as apicoplast proteins by inference from direct assay (IDA). In addition, 30% of the nuclear-encoded translational genes that are not coexpressed with the known cytoplasmic machinery are found within this small group of genes. More importantly, 76 ORFs (62%) are of unknown function, with little or no homology to other genes. This limited subgroup of putative plastid-targeted ORFs are likely excellent candidates for further studies in the ongoing search for malaria-specific functions as putative drug targets.

Figure 4 Temporal Distribution of the Apicoplast-Targeted Proteins and P. falciparum Proteases, Potential Antimalarial Drug Candidates
(A) The expression profiles of all putative plastid-targeted genes represented on our microarray are shown. The yellow box encompasses a highly synchronized group of genes, which are in-phase with plastid genome expression. The average expression profile for this in-phase group of genes is shown and includes most of the known apicoplast-targeted genes as well as many hypothetical genes. For reference, the average expression profile for the plastid genome is shown (dashed gray line).

(B) Proteases represent an attractive target for chemotherapeutic development. The broad range of temporal expression for various classes of proteases and their putative functions are displayed.

Abbreviations: HAP, histo-aspartyl protease (PM III); Clp, caseineolytic protease; sub1, 2, subtilisin-like protease 1 and 2.

Similarly, P. falciparum proteases have received much attention, since they are candidates as drug targets and have been shown to play important roles in regulation as well as metabolism throughout the IDC (Rosenthal 2002). A temporal ordering of expression profiles for several well-characterized P. falciparum proteases is shown in Figure 4B, demonstrating the broad significance of these enzymes throughout the IDC. One of the principal proteolytic functions is considered to be the degradation of host cell hemoglobin in the food vacuole (FV) to produce amino acids essential for protein synthesis. This elaborate process is carried out by a series of aspartyl proteases, cysteine proteases, metalloproteases, and aminopeptidases (Francis et al. 1997).

A family of ten aspartyl proteases, the plasmepsins (PMs), has been identified in the P. falciparum genome, four of which have been characterized as bona fide hemoglobinases: PM I, II, III (a histo-aspartic protease [HAP]), and IV (Coombs et al. 2001). Our data reveal that the PMs are expressed at different times throughout the lifecycle, suggesting that they are involved in different processes throughout the IDC. PM I, II, HAP, and PM IV are adjacent to one another on Chromosome 14 and have been localized to the FV. While HAP and PM II are expressed in the mid-trophozoite stage, during peak hemoglobin catabolism, PMI and IV are maximally expressed in the ring stage along with the cysteine protease falcipain-1 (FP-1). FP-1 has recently been implicated in merozoite invasion and has been localized to the interior of the PV (Greenbaum et al. 2002). The coincident expression of these proteases implies that the development of the PV and the FV occurs during the very early-ring stage. This observation is corroborated by similar expression profiles for the PV-associated protein RESA1 and the FV protein PGH1. Subsequently, a second group of hemoglobinases, including the m1-family aminopeptidase, FP-2, and falcilysin, is expressed simultaneously with HAP and PM II during the trophozoite stage of the IDC. The expression of PM V and the newly identified FP- 2 homologue during this stage suggests they are also important in the trophozoite stage. The other known falcipain, FP-3, does not show a marked induction in expression throughout the IDC. We fail to detect any transcripts for PM VI, VII, and VIII during the IDC. These genes may have roles in any of the other sexual, liver, or mosquito stages of development.

In addition to the hemoglobinases, P. falciparum contains a variety of proteases involved in cellular processing, including a group of Clps and signal peptidases that are all expressed maximally at the late-trophozoite stage (Figure 4B). The timing of these genes may play a key role in protein maturation during trafficking to various compartments, including the plastid. The three Clps contain putative leader peptides and may actually function within the plastid. Finally, a group of proteases are expressed in the schizont stage and include the P. falciparum subtilisin-like proteases PfSUB1 and PfSUB2 as well as PMs IX and X. PfSUB1 and PfSUB2 are believed to be involved in merozoite invasion and have been localized apically in the dense granules. Interestingly, there are two PfSUB1 protease homologues (PFE0355c and PFE0370c); PM X parallels the expression of PfSUB1 (PFE0370c), suggesting that aspartyl proteases may also be involved in merozoite invasion. In addition, the phase of the PfSUB1 homologue suggests a concomitant role, with PM IX slightly preceding merozoite invasion. In total, we have detected gene expression for over 80 putative proteases throughout the entire IDC (Table S6). This set includes over 65 proteases from a group of recently predicted proteases (Wu et al. 2003). The differing temporal expression of these proteases may allow for a multifaceted approach toward identifying protease inhibitors with efficacy at all stages of the IDC.

Implications for New Vaccine Therapies
Merozoite invasion is one of the most promising target areas for antimalarial vaccine development (Good 2001). Many vaccine efforts thus far have focused primarily on a set of plasmodial antigens that facilitate receptor–ligand interaction between the parasite and the host cell during the invasion process (Preiser et al. 2000) (see Figure 2K and 2M). Merozoite invasion antigens are contributing factors to naturally acquired immunity, triggering both humoral and antibody-independent cell-mediated responses (Good and Doolan 1999). Antibodies against these antigens have been demonstrated to effectively block the merozoite invasion process in vitro and in animal models (Ramasamy et al. 2001). Owing to the highly unique character of merozoite surface antigens, homology-based searches have yielded only a limited set of additional invasion factors.

We utilized the IDC transcriptome to predict a set of likely invasion proteins by identifying expression profiles with characteristics similar to previously studied merozoite invasion proteins. The expression profiles for all known invasion factors undergo a sharp induction during the mid- to late-schizont stage and are characterized by large expression amplitudes (see Figure 2A). Among these proteins are seven of the best-known malaria vaccine candidates, including AMA1, MSP1, MSP3, MSP5, EBA175, RAP1, and RESA1. To identify ORFs with a possible involvement in the merozoite invasion process, we have calculated the similarity, by Euclidian distance, between the expression profiles of these seven vaccine candidates and the rest of the IDC transcriptome. A histogram of the distance values reveals a bimodal distribution with 262 ORFs in the first peak of the distribution (Figure S4). This represents the top 5% of expression profiles when ranked by increasing Euclidian distance (Table S7). In addition to the seven vaccine candidate genes used for the search, essentially all predicted P. falciparum merozoite-associated antigens were identified in this gene set (Figure 5). These include the GPI-anchored MSP4; several integral merozoite membrane proteins, such as EBA140 and EBL1; three RBPs (RBP1, RBP2a, RBP2b); and a previously unknown RBP homologue. In addition, components of two proteins secreted from the rhoptries to the host cell membranes, RhopH1 and RhopH3, or to the PVs RAP1, RAP2, and RAP3 were found in the selected set. Surprisingly, CLAG2 and CLAG9 were also classified into the merozoite invasion group. Although the biological function of these genes is believed to be associated with cytoadherence of the infected erythrocyte to the vascular endothelium, a highly related homologue, CLAG3.1 (RhopH1), was recently detected in the rhoptries, suggesting a possible secondary role for these genes in merozoites (Kaneko et al. 2001).

Figure 5 Phaseogram of Putative Vaccine Targets
The similarity of all expression profiles to seven known vaccine candidates (boxed) was calculated. The top 5% of similar profiles correspond to 262 ORFs, 28 of which have been previously associated with plasmodial antigenicity and the process of merozoite invasion.

A number of antigens are presently in various stages of clinical trials and are yielding encouraging results (Good et al. 1998). However, many single-antigen vaccine studies indicate that the most promising approach will require a combination of antigenic determinants from multiple stages of the complex plasmodial lifecycle (Kumar et al. 2002). Searches for new target antigens in the P. falciparum genome are thus vital to the development of future vaccines, since no fully protective vaccine has been assembled thus far. Of the 262 ORFs whose expression profiles were closest to the profiles of the seven major vaccine candidates, 189 are of unknown function. These ORFs represent a candidate list for new vaccine targets.

Discussion
The transcriptome of the IDC of P. falciparum constitutes an essential tool and baseline foundation for the analysis of all future gene expression studies in this organism, including response to drugs, growth conditions, environmental perturbations, and genetic alterations. Essentially all experiments involving asexual intraerythrocytic-stage parasites must be interpreted within the context of the ongoing cascade of IDC-regulated genes.

In our global analysis of the P. falciparum transcriptome, over 80% of the ORFs revealed changes in transcript abundance during the maturation of the parasite within RBCs. The P. falciparum IDC significantly differs from the cell cycles of the yeast S. cerevisiae (Spellman et al. 1998) and human HeLa (Whitfield et al. 2002) cells, during which only 15% of the total genome is periodically regulated. Instead, the P. falciparum IDC resembles the transcriptome of the early stages of Drosophila melanogaster development, which incorporates the expression of over 80% of its genome as well (Arbeitman et al. 2002). Unlike the development of multicellular eukaryotes, there is no terminal differentiation and, with the exception of gametocytogenesis, the parasite is locked into a repeating cycle. In this respect, the P. falciparum IDC mirrors a viral-like lifecycle, in which a relatively rigid program of transcriptional regulation governs the progress of the course of infection.

The lack of continuous chromosomal domains with common expression characteristics suggests that the genes are regulated individually, presumably via distinct sets of cis- and trans-acting elements. However, the extent and the simple mechanical character of transcriptional control observed in the IDC suggest a fundamentally different mode of regulation than what has been observed in other eukaryotes. It is plausible that a comparatively small number of transcription factors with overlapping binding site specificities could account for the entire cascade. While further experiments are ongoing, it may be the case that P. falciparum gene regulation is streamlined to the extent that it has lost the degree of dynamic flexibility observed in other unicellular organisms, from Escherichia coli to yeast. This observation also implies that disruption of a key transcriptional regulator, as opposed to a metabolic process, may have profound inhibitory properties. While a few putative transcription factors have been identified in the P. falciparum genome, no specific regulatory elements have been defined in basepair-level detail. A further analysis of the upstream regions of genes with similar phases should facilitate the elucidation of regulatory regions and their corresponding regulatory proteins.

In general, the timing of mRNA expression for a given gene during the IDC correlates well with the function of the resultant protein. For example, replication of the genome occurs in the early-schizont stage and correlates well with the peak expression of all factors of DNA replication and DNA synthesis. Also, organellar biogenesis of several intracellular compartments such as mitochondria, the plastid, or the apical invasion organelles is concomitant with the maximal induction of mRNAs encoding proteins specific to these organelles. In addition, our data are generally in good agreement with proteomic analyses that have detected intraerythrocytic-stage proteins from the merozoite, trophozoite, and schizont stages. More than 85% of the 1,588 proteins detected in these studies were also expressed in our analysis (Florens et al. 2002; Lasonder et al. 2002). However, a more detailed proteomic analysis at different stages of the IDC will be needed to ascertain the temporal changes of these proteins.

We initially expected that a high percentage of the genome would be specialized for each lifecycle stage (mosquito, liver, blood), yet this was not observed; the mRNA transcripts for 75% of proteins determined to be gamete-, gametocyte-, or sporozoite-specific by mass spectrometry are also transcribed in the plasmodial IDC. These findings confirm previous studies demonstrating that not only genes used for generic cellular processes are present in multiple developmental stages, but also factors of highly specialized Plasmodium functions (Gruner et al. 2001). This may indicate that only a small portion of the genome may actually be truly specific to a particular developmental stage and that the majority of the genome is utilized throughout the full lifecycle of this parasite. It is also feasible to speculate that a multilayer regulatory network is employed in the progression of the entire P. falciparum lifecycle. In this model, the same cis- and trans-acting regulatory elements driving the actual mRNA production in IDC are utilized in other developmental stages. These elements are then controlled by an alternate subset of factors determining the status of the lifecycle progression.

These findings also outline two contrasting properties of the P. falciparum genome. The Plasmodium parasite devotes 3.9% of its genome to a complex system of antigenic determinants essential for host immune evasion during a single developmental stage (Gardner et al. 2002). On the other hand, large portions of the genome encode proteins used in multiple stages of the entire lifecycle. Such broad-scope proteins might be excellent targets for both vaccine and chemotherapeutic antimalarial strategies, since they would target several developmental stages simultaneously. While there are certainly proteins specific to these nonerythrocytic stages, a complementary analysis of both proteomic and genomic datasets will facilitate the search.

With malaria continuing to be a major worldwide disease, advances toward understanding the basic biology of P. falciparum remain essential. Our analysis of the IDC transcriptome provides a first step toward a comprehensive functional analysis of the genome of P. falciparum. The genome-wide transcriptome will be useful not only for the further annotation of many uncharacterized genes, but also for defining the biological processes utilized by this highly specialized parasitic organism. Importantly, candidate groups of genes can be identified that are both functionally and transcriptionally related and thus provide focused starting points for the further elucidation of genetic and mechanistic aspects of P. falciparum. Such biological characterizations are presently a major objective in the search for novel antimalarial strategies. The public availability of the dataset presented in this study is intended to provide a resource for the entire research community to extend the exploration of P. falciparum beyond the scope of this publication. All data will be freely accessible at two sites: http://plasmodb.org and http://malaria.ucsf.edu.

Materials and Methods

Cell culture.
A large-scale culture of P. falciparum (HB3 strain) was grown in a standard 4.5 l microbial bioreactor (Aplikon, Brauwweg, Netherlands) equipped with a Bio Controller unit ADI 1030 (Aplikon, Brauwweg, Netherlands). Cells were initially grown in a 2% suspension of purified human RBCs and RPMI 1640 media supplemented with 0.25% Albumax II (GIBCO, Life Technologies, San Diego, California, United States), 2 g/l sodium bicarbonate, 0.1 mM hypoxanthine, 25 mM HEPES (pH 7.4), and 50 μg/l gentamycin, at 37°C, 5% O2, and 6% CO2. Cells were synchronized by two consecutive sorbitol treatments for three generations, for a total of six treatments. Large-scale cultures contained 32.5 mM HEPES (pH 7.4). The bioreactor culture was initiated by mixing 25.0 ml of parasitized RBCs (20% late schizonts, approximately 45 hpi) with an additional 115.0 ml of purified RBC in a total of 1.0 l of media (14% hematocrit). Invasion of fresh RBCs occurred during the next 2 h, raising the total parasitemia from an initial 5% to 16%. After this period, the volume of the culture was adjusted to 4.5 l, bringing the final RBC concentration to approximately 3.3% to reduce the invasion of remaining cells. Immediately after the invasion period, greater than 80% of the parasites were in the ring stage. Temperature and gas conditions were managed by the Bio Controller unit. Over the course of 48 h, 3–4 ml of parasitized RBCs was collected every hour, washed with prewarmed PBS, and flash-frozen in liquid nitrogen.

RNA preparation and reference pool.

P. falciparum RNA sample isolation, cDNA synthesis, labeling, and DNA microarray hybridizations were performed as described by Bozdech et al. (2003). Samples for individual timepoints (coupled to Cy5) were hybridized against a reference pool (coupled to Cy3). The reference pool was comprised of RNA samples representing all developmental stages of the parasite. From this pool, sufficient cDNA synthesis reactions, using 12 μg of pooled reference RNA, were performed for all hybridizations. After completing cDNA synthesis, all reference pool cDNAs were combined into one large pool and then split into individual aliquots for subsequent labeling and hybridization. Microarray hybridizations were incubated for 14–18 h.

DNA microarray hybridizations and quality control.
In total, 55 DNA microarray hybridizations covering 46 timepoints were performed. Timepoints 1, 7, 11, 14, 18, 20, 27, and 31 were represented by more than one array hybridization. Data were acquired and analyzed by GenePix Pro 3 (Axon Instruments, Union City, California, United States). Array data were stored and normalized using the NOMAD microarray database system (http://ucsf-nomad.sourceforge.net/). In brief, a scalar normalization factor was calculated for each array using unflagged features with median intensities greater than zero for each channel and a pixel regression correlation coefficient greater than or equal to 0.75. Quality spots were retained based on the following criteria. The log2(Cy5/Cy3) ratio for array features that were unflagged and had a sum of median intensities greater than the local background plus two times the standard deviation of the background were extracted from the database for further analysis. Subsequently, expression profiles consisting of 43 of 46 timepoints (approximately 95%) were selected. For those timepoints that were represented by multiple arrays, the ratio values were averaged.

FFT analysis of the expression profiles.
Fourier analysis was performed on each profile in the quality-controlled set (5,081 oligonucleotides). Profiles were smoothed with missing values imputed using a locally weighted regression algorithm with local weighting restricted to 12% using R (http://www.R-project.org). Fourier analysis was performed on each profile using the fft() function of R, padded with zeros to 64 measurements. The power spectrum was calculated using the spectrum() function of R. The power at each frequency (Power()), the total power (Ptot), and the frequency of maximum power (Fmax) were determined. The periodicity score was defined as Power[(Fmax−1) + (Fmax) + (Fmax+1)]/Ptot. The most frequent value of Fmax across all profiles was deemed the major frequency (m) and used in determining phase information. The phase of each profile was calculated as atan2\[−(I (m)],R (m)\, where atan2 is R's arctangent function and I and R are the imaginary and real parts of the FFT. Profiles were then ordered in increasing phase from −π to π. The loess smooth profiles were drawn through the raw expression data using the loess() function found in the modern regression library of R (version 1.5.1). The default parameters were used, with the exception that local weighting was reduced to 30%. For the averaged profiles of the functional groups (see Figure 2B–2M), the loess smooth profiles were calculated for each expression profile individually and subsequently averaged to create the representative profile. These same methods were applied to both the randomized set (see the inset to Figure 1F) and the yeast cell cycle dataset (see Figure S1).

The raw results files (Dataset S1), the fully assembled raw dataset (Dataset S2, the overview dataset (Dataset S3, and the quality control dataset (Dataset S4) are available as downloads.

Evaluation of coexpression along chromosomes.
The evaluation of coexpression of genes along chromosomes was carried out as follows. The Pearson correlation coefficient was calculated for each pair of profiles. For ORFs with multiple oligonucleotides, the average profile was calculated. The neighborhood of each ORF profile was defined as a window of between one and ten adjacent ORF profiles. If any window in an ORF profile's neighborhood displayed more than 70% pairwise correlation of greater than 0.75, it was flagged as enriched. The length of the window was then recorded as a region of coexpression. This process was repeated without strand separation of ORFs and with randomly permuted datasets.

Comparative genomic hybridization.

P. falciparum strains 3D7 and HB3 were cultured as previously described at a concentration of 10% parasitaemia. Genomic DNA (gDNA) was isolated from a minimum of 500 ml of total culture for each P. falciparum strain, as previously described (Wang et al. 2002). Isolated gDNA from each strain was sheared by sonication to an average fragment size of approximately 1–1.5 kb and then was purified and concentrated using a DNA Clean and Concentrator kit (Zymo Research, Orange, California, United States). Amino-allyl-dUTP first was incorporated into the gDNA fragments with a Klenow reaction at 37°C for 6–8 h with random nonamer primers and 3 μg of sheared gDNA. After purification and concentration of the DNA from the Klenow reaction, CyScribe Cy3 and Cy5 dyes (Amersham Biosciences, Buckinghamshire, United Kingdom) were coupled to HB3 DNA and 3D7 DNA, respectively, as previously described (Pollack et al. 1999). Uncoupled fluorescent dye was removed using a DNA Clean and Concentrator kit. Labeled DNA fragments were hybridized to the oligonucleotide-based DNA microarrays. Fluorescence was detected and analyzed using an Axon Instruments scanner and GenePix Pro 3.0 software. Only features that had median intensities greater than the local background plus two times the standard deviation of the background in each channel were considered for further analysis. For each feature, the percent of the total intensity was determined using the signal in the 3D7 channel as the total amount of intensity for each oligonucleotide; intensity differences less than 50% were considered to be significant for subsequence analysis.

Calculation for in-phase plastid-targeted genes.
The range of FFT-based phases for the expression profiles of the plastid genome is between 0.32 and 1.05 (or roughly π/9 −π/3). Using the list of 551 apicoplast-targeted genes available at PlasmoDB.org, we first ordered these genes by phase and then grouped all genes with a phase range between 0.00 and 1.40 (0–4π/9), resulting in 124 genes represented by 128 oligonucleotides on the microarray. This select group represents the in-phase plastid targeted genes (see Table S6).

Calculation for vaccine targets.
To select the expression profiles most related to the AMA1, MSP1, MSP3, MSP5, EBA175, RAP1, and RESA1 vaccine candidates, we calculated the similarity of all expression profiles in the dataset to those of these antigens by Euclidian distance. The minimum Euclidian distance calculated for every profile was then binned into 60 bins and plotted as a histogram. A natural break in the histogram was seen that included the set of 262 ORFs (see Figure S2).

Supporting Information
Dataset S1 Raw GenePix Results
(29.5 MB ZIP).

Click here for additional data file.

 Dataset S2 Complete Dataset
(3.7 MB TXT).

Click here for additional data file.

 Dataset S3 Overview Dataset
(2.4 MB TXT).

Click here for additional data file.

 Dataset S4 Quality Control Set
(3.1 MB TXT).

Click here for additional data file.

 Figure S1 Histogram of the Percent Power at Peak Frequencies for the Yeast Cell Cycle Data
The percent of power in the maximum frequency of the FFT power spectrum was used to determine periodicity of the yeast cell cycle data from Spellman et al. (1998). The histogram reveals periodic regulation of gene expression for only a small subset of genes (% power >70%).

(223 KB EPS).

Click here for additional data file.

 Figure S2 Pearson Correlation Maps for the P. falciparum Chromosomes
A matrix of the pairwise Pearson correlations was calculated for every expression profile along the chromosomes. The analysis included all annotated ORFs. The gray areas correspond to a Pearson correlation d(x, y) = 0 and indicate ORFs with no detectable IDC expression or ORFs not represented on the microarray. The starting point (left) and the end point (right) of the chromosomes and the ORF order along the chromosomes are identical to the order in PlasmoDB.org.

(30.9 MB EPS).

Click here for additional data file.

 Figure S3 CGH of 3D7 versus HB3 for All Chromosomes
Genomic differences between strain 3D7 and strain HB3 were measured by CGH. The relative hybridization between the gDNA derived from these two strains is shown as a percent reduction of the signal intensity for 3D7 along individual chromosomes. (1.7 MB ZIP).

Click here for additional data file.

 (A) (216 KB EPS)
Click here for additional data file.

 (B) (232 KB EPS)
Click here for additional data file.

 (C) (237 KB EPS)
Click here for additional data file.

 (D) (240 KB EPS)
Click here for additional data file.

 (E) (252 KB EPS)
Click here for additional data file.

 (F) (232 KB EPS)
Click here for additional data file.

 (G) (235 KB EPS)
Click here for additional data file.

 (H) (235 KB EPS)
Click here for additional data file.

 (I) (249 KB EPS)
Click here for additional data file.

 (J) (265 KB EPS)
Click here for additional data file.

 (K) (283 KB EPS)
Click here for additional data file.

 (L) (270 KB EPS)
Click here for additional data file.

 (M) (305 KB EPS)
Click here for additional data file.

 (N) (332 KB EPS)
Click here for additional data file.

 Figure S4 Distribution of Euclidian Distances between Expression Profiles of the IDC Genes and Seven Vaccine Candidates
The similarity between each IDC expression profile and the profiles of the seven selected vaccine candidate genes was evaluated by Euclidian distance calculations, d(x,y) = Σ(xi − yi)2. The Euclidian distance value to the closest vaccine homologue was selected for each IDC profile and used to generate this plot. Genes with d(x,y) < 20 were selected for the phaseogram of putative vaccine targets (see Figure 5).

(494.02 KB EPS).

Click here for additional data file.

 Table S1 Pearson Correlation for ORFs Represented by Multiple Oligonucleotides
This table contains all of the ORFs in the analyzed dataset that are represented by multiple oligonucleotides on the DNA microarray. The average Pearson correlation value has been calculated for the expression profiles of all oligonucleotides for each given ORF.

(44 KB TXT).

Click here for additional data file.

 Table S2 
P. falciparum Functional Gene Groups
This table contains all of the P. falciparum groups discussed. The groups include the following: transcription machinery, cytoplasmic translation machinery, the glycolytic pathway, ribonucleotide synthesis, deoxyribonucleotide synthesis, DNA replication machinery, the TCA cycle, the proteaseome, the plastid genome, merozoite invasion, actin–myosin motility, early-ring transcripts, mitochondrial genes, and the organellar translational group.

(291 KB TXT).

Click here for additional data file.

 Table S3 Coregulation along the Chromosomes of P. falciparum

This table contains the regions of coregulation found in the chromosomes of P. falciparum determined by calculating the Pearson correlation between expression profiles for contiguous ORFs. The cutoff was 70% pairwise correlation of greater than 0.75 for each group. Only groups of two ORFs or more are listed.

(6 KB TXT).

Click here for additional data file.

 Table S4 3D7 versus HB3 CGH Data
This table contains all of the intensity data from CGH of gDNA derived from the 3D7 and HB3 strains of P. falciparum. The averaged intensities from three microarray hybridization experiments are listed.

(414 KB TXT).

Click here for additional data file.

 Table S5 Putative Apicoplast-Targeted Genes and Expression Profiles
This table contains all of the predicted apicoplast-targeted ORFs from PlasmoDB.org. The presence of each ORF on the DNA microarray is tabulated, as well as whether each ORF is present in the overview set. Finally, the plastid ORFs in-phase with plastid genome expression are listed, as well as the corresponding oligonucleotide identifiers.

(147 KB TXT).

Click here for additional data file.

 Table S6 Putative P. falciparum Proteases and Their Expression Data
The table was constructed by searching the database for any putative protease annotations and contains all of the 92 proteases identified by Wu et al. (2003).

(59 KB TXT).

Click here for additional data file.

 Table S7 Vaccine Candidate Correlation Table
The similarity of all expression profiles to seven known vaccine candidates was evaluated by a Euclidian distance calculation to all expression profiles measured. These 262 ORFs constitute the top 5% of genes in the IDC with minimum distance to these seven ORFs. The seven candidates used are AMA1, MSP1, MSP3, MSP5, EBA175, RAP1, and RESA1.

(204 KB TXT).

Click here for additional data file.

 We would like to thank Ashwini Jambhekar, Pradip K. Rathod, David S. Roos, Phil J. Rosenthal, Anita Sil, Akhil Vaidya, and Dave Wang for critical comments. For technical assistance, we thank Takeshi Irie, Terry Minn, and Samara L. Reck-Peterson. This work was supported by the Burroughs-Wellcome Fund, the Kinship Foundation, a Sandler Opportunity Grant, and National Institute of Allergy and Infectious Diseases grant AI53862.


Conflicts of Interest. The authors have declared that no conflicts of interest exist.


Author Contributions. ZB, ML, and JLD conceived and designed the experiments. ZB, ML, and EDW performed the experiments. ZB, ML, BLP, EDW, JZ, and JLD analyzed the data. BLP and JZ contributed reagents/materials/analysis tools. ZB, ML, BLP, EDW, and JLD wrote the paper.

Academic Editor: Gary Ward, University of Vermont.

Abbreviations
ASLadenylosuccinate lyase

CGHcomparative genomic hybridization

CLAGcytoadherence-linked asexual gene

Clpcaseineolytic protease

DHFR-TSdihydrofolate reductase–thymidylate synthetase

EBAerythrocyte-binding antigen

EBLerythrocyte-binding-like protein

FFTfast Fourier transform

FPfalcipain

FVfood vacuole

gDNAgenomic DNA

HAPhisto-aspartyl protease

hpihours postinvasion

IDCintraerythrocytic developmental cycle

MSPmerozoite surface protein

ORFopen reading frame

PMplasmepsin

PVparasitophorous vacuole

RBCred blood cell

RBPreticulocyte-binding protein

RESAring-infected surface antigen

SERAserine repeat antigen

TCAtricarboxylic acid.
==== Refs
References
Afonso Nogueira P  Wunderlich G  Shugiro Tada M  d'Arc Neves Costa J  Jose Menezeset M    
Plasmodium falciparum : Analysis of transcribed var  gene sequences in natural isolates from the Brazilian Amazon region Exp Parasitol 2002 101 111 120 12427465 
Arbeitman MN  Furlong EE  Imam F  Johnson E  Null BH    Gene expression during the life cycle of Drosophila melanogaster 
 Science 2002 297 2270 2275 12351791 
Bahl A  Brunk B  Crabtree J  Fraunholz MJ  Gajria B    PlasmoDB: The Plasmodium  genome resource: A database integrating experimental and computational data Nucleic Acids Res 2003 31 212 215 12519984 
Ben Mamoun C  Gluzman IY  Hott C  MacMillan SK  Amarakone AS    Co-ordinated programme of gene expression during asexual intraerythrocytic development of the human malaria parasite Plasmodium falciparum  revealed by microarray analysis Mol Microbiol 2001 39 26 36 11123685 
Blackman MJ   Proteases involved in erythrocyte invasion by the malaria parasite: Function and potential as chemotherapeutic targets Curr Drug Targets 2000 1 59 83 11475536 
Bozdech Z  Zhu J  Joachimiak MP  Cohen FE  Pulliam B    Expression profiling of the schizont and trophozoite stages of Plasmodium falciparum  with a long-oligonucleotide microarray Genome Biol 2003 4 R9 12620119 
Cheng Q  Cloonan N  Fischer K  Thompson J  Waine G    
stevor  and rif  are Plasmodium falciparum  multicopy gene families which potentially encode variant antigens Mol Biochem Parasitol 1998 97 161 176 9879895 
Coombs GH  Goldberg DE  Klemba M  Berry C  Kay J    Aspartic proteases of Plasmodium falciparum  and other parasitic protozoa as drug targets Trends Parasitol 2001 17 532 537 11872398 
Cowman AF  Baldi DL  Healer J  Mills KE  O'Donnell RA    Functional analysis of proteins involved in Plasmodium falciparum  merozoite invasion of red blood cells FEBS Lett 2000 476 84 88 10878256 
Deitsch KW  Calderwood MS  Wellems TE   Malaria: Cooperative silencing elements in var  genes Nature 2001 412 875 876 
Dluzewski AR  Garcia CR   Inhibition of invasion and intraerythrocytic development of Plasmodium falciparum  by kinase inhibitors Experientia 1996 52 621 623 8698101 
Eisen MB  Brown PO   DNA arrays for analysis of gene expression Methods Enzymol 1999 303 179 205 10349646 
Feagin JE  Gardner MJ  Williamson DH  Wilson RJ   The putative mitochondrial genome of Plasmodium falciparum 
 J Protozool 1991 38 243 245 1880762 
Fichera ME  Roos DS   A plastid organelle as a drug target in apicomplexan parasites Nature 1997 390 407 409 9389481 
Florens L  Washburn MP  Raine JD  Anthony RM  Grainger M    A proteomic view of the Plasmodium falciparum  life cycle Nature 2002 419 520 526 12368866 
Foley M  Tilley L  Sawyer WH  Anders RF   The ring-infected erythrocyte surface antigen of Plasmodium falciparum  associates with spectrin in the erythrocyte membrane Mol Biochem Parasitol 1991 46 137 147 1852169 
Foth BJ  Ralph SA  Tonkin CJ  Struck NS  Fraunholz M    Dissecting apicoplast targeting in the malaria parasite Plasmodium falciparum 
 Science 2003 299 705 708 12560551 
Fox BA  Li WB  Tanaka M  Inselburg J  Bzik DJ   Molecular characterization of the largest subunit of Plasmodium falciparum  RNA polymerase I Mol Biochem Parasitol 1993 61 37 48 8259131 
Francis SE  Sullivan DJ Jr  Goldberg DE   Hemoglobin metabolism in the malaria parasite Plasmodium falciparum 
 Annu Rev Microbiol 1997 51 97 123 9343345 
Gardner MJ  Hall N  Fung E  White O  Berriman M    Genome sequence of the human malaria parasite Plasmodium falciparum 
 Nature 2002 419 498 511 12368864 
Gero AM  O'Sullivan WJ   Purines and pyrimidines in malarial parasites Blood Cells 1990 16 467 484 2257323 
Good MF   Towards a blood-stage vaccine for malaria: Are we following all the leads? Nat Rev Immunol 2001 1 117 125 11905819 
Good MF  Doolan DL   Immune effector mechanisms in malaria Curr Opin Immunol 1999 11 412 419 10448141 
Good MF  Kaslow DC  Miller LH   Pathways and strategies for developing a malaria blood-stage vaccine Annu Rev Immunol 1998 16 57 87 9597124 
Gray JW  Collins C   Genome changes and gene expression in human solid tumors Carcinogenesis 2000 21 443 452 10688864 
Greenbaum DC  Baruch A  Grainger M  Bozdech Z  Medzihradszky KF    A role for the protease falcipain 1 in host cell invasion by the human malaria parasite Science 2002 298 2002 2006 12471262 
Gruner AC  Brahimi K  Eling W  Konings R  Meis J    The Plasmodium falciparum  knob-associated PfEMP3 antigen is also expressed at preerythrocytic stages and induces antibodies which inhibit sporozoite invasion Mol Biochem Parasitol 2001 112 253 261 11223132 
Hayward RE  DeRisi JL  Alfadhli S  Kaslow DC  Brown PO    Shotgun DNA microarrays and stage-specific gene expression in Plasmodium falciparum  malaria Mol Microbiol 2000 35 6 14 10632873 
Horrocks P  Dechering K  Lanzer M   Control of gene expression in Plasmodium falciparum 
 Mol Biochem Parasitol 1998 95 171 181 9803410 
Jomaa H  Wiesner J  Sanderbrand S  Altincicek B  Weidemeyer C    Inhibitors of the nonmevalonate pathway of isoprenoid biosynthesis as antimalarial drugs Science 1999 285 1573 1576 10477522 
Kaneko O  Tsuboi T  Ling IT  Howell S  Shirano M    The high molecular mass rhoptry protein, RhopH1, is encoded by members of the clag  multigene family in Plasmodium falciparum  and Plasmodium yoelii 
 Mol Biochem Parasitol 2001 118 223 231 11738712 
Kissinger JC  Brunk BP  Crabtree J  Fraunholz MJ  Gajria B    The Plasmodium  genome database Nature 2002 419 490 492 12368860 
Kumar S  Epstein JE  Richie TL  Nkrumah FK  Soisson L    A multilateral effort to develop DNA vaccines against falciparum malaria Trends Parasitol 2002 18 129 135 11854091 
Lang-Unnasch N   Purification and properties of Plasmodium falciparum  malate dehydrogenase Mol Biochem Parasitol 1992 50 17 25 1542310 
Lasonder E  Ishihama Y  Andersen JS  Vermunt AM  Pain A    Analysis of the Plasmodium falciparum  proteome by high-accuracy mass spectrometry Nature 2002 419 537 542 12368870 
Le Roch KG  Zhou Y  Batalov S  Winzeler EA   Monitoring the chromosome 2 intraerythrocytic transcriptome of Plasmodium falciparum  using oligonucleotide arrays Am J Trop Med Hyg 2002 67 233 243 12408661 
Li WB  Bzik DJ  Gu HM  Tanaka M  Fox BA    An enlarged largest subunit of Plasmodium falciparum  RNA polymerase II defines conserved and variable RNA polymerase domains Nucleic Acids Res 1989 17 9621 9636 2690004 
Li WB  Bzik DJ  Tanaka M  Gu HM  Fox BA    Characterization of the gene encoding the largest subunit of Plasmodium falciparum  RNA polymerase III Mol Biochem Parasitol 1991 46 229 239 1656254 
McFadden GI  Roos DS   Apicomplexan plastids as drug targets Trends Microbiol 1999 7 328 333 10431206 
Miller SK  Good RT  Drew DR  Delorenzi M  Sanders PR    A subset of Plasmodium falciparum  SERA genes are expressed and appear to play an important role in the erythrocytic cycle J Biol Chem 2002 277 47524 47532 12228245 
Myler PJ  Beverley SM  Cruz AK  Dobson DE  Ivens AC    The Leishmania  genome project: New insights into gene organization and function Med Microbiol Immunol (Berl) 2001 190 9 12 11770120 
Opitz C  Soldati D   “The glideosome”: A dynamic complex powering gliding motion and host cell invasion by Toxoplasma gondii 
 Mol Microbiol 2002 45 597 604 12139608 
Patankar S  Munasinghe A  Shoaibi A  Cummings LM  Wirth DF   Serial analysis of gene expression in Plasmodium falciparum  reveals the global expression profile of erythrocytic stages and the presence of anti-sense transcripts in the malarial parasite Mol Biol Cell 2001 12 3114 3125 11598196 
Pinder J  Fowler R  Bannister L  Dluzewski A  Mitchell GH   Motile systems in malaria merozoites: How is the red blood cell invaded? Parasitol Today 2000 16 240 245 10827429 
Pollack JR  Perou CM  Alizadeh AA  Eisen MB  Pergamenschikov A    Genome-wide analysis of DNA copy-number changes using cDNA microarrays Nat Genet 1999 23 41 46 10471496 
Pollack JR  Sorlie T  Perou CM  Rees CA  Jeffrey SS    Microarray analysis reveals a major direct role of DNA copy number alteration in the transcriptional program of human breast tumors Proc Natl Acad Sci U S A 2002 99 12963 12968 12297621 
Preiser P  Kaviratne M  Khan S  Bannister L  Jarra W   The apical organelles of malaria merozoites: Host cell selection, invasion, host immunity and immune evasion Microbes Infect 2000 2 1461 1477 11099933 
Ramasamy R  Ramasamy M  Yasawardena S   Antibodies and Plasmodium falciparum  merozoites Trends Parasitol 2001 17 194 197 11282510 
Reyes P  Rathod PK  Sanchez DJ  Mrema JE  Rieckmann KH    Enzymes of purine and pyrimidine metabolism from the human malaria parasite, Plasmodium falciparum 
 Mol Biochem Parasitol 1982 5 275 290 6285190 
Ridley RG   Medical need, scientific opportunity and the drive for antimalarial drugs Nature 2002 415 686 693 11832957 
Rosenthal PJ   Hydrolysis of erythrocyte proteins by proteases of malaria parasites Curr Opin Hematol 2002 9 140 145 11844998 
Roy A  Cox RA  Williamson DH  Wilson RJ   Protein synthesis in the plastid of Plasmodium falciparum 
 Protist 1999 150 183 188 10505417 
Sachs J  Malaney P   The economic and social burden of malaria Nature 2002 415 680 685 11832956 
Sherman I   Malaria: Parasite biology, pathogenesis, and protection 1998 Washington, DC American Society for Microbiology 
Spellman PT  Sherlock G  Zhang MQ  Iyer VR  Anders K    Comprehensive identification of cell cycle–regulated genes of the yeast Saccharomyces cerevisiae  by microarray hybridization Mol Biol Cell 1998 9 3273 3297 9843569 
Troye-Blomberg M  Riley EM  Perlmann H  Andersson G  Larsson A    T and B cell responses of Plasmodium falciparum  malaria-immune individuals to synthetic peptides corresponding to sequences in different regions of the P. falciparum  antigen Pf155/RESA J Immunol 1989 143 3043 3048 2478632 
Waller RF  Keeling PJ  Donald RG  Striepen B  Handman E    Nuclear-encoded proteins target to the plastid in Toxoplasma gondii  and Plasmodium falciparum 
 Proc Natl Acad Sci U S A 1998 95 12352 12357 9770490 
Waller RF  Reed MB  Cowman AF  McFadden GI   Protein trafficking to the plastid of Plasmodium falciparum  is via the secretory pathway EMBO J 2000 19 1794 1802 10775264 
Walliker D  Quakyi IA  Wellems TE  McCutchan TF  Szarfman A    Genetic analysis of the human malaria parasite Plasmodium falciparum 
 Science 1987 236 1661 1666 3299700 
Wang P  Wang Q  Sims PF  Hyde JE   Rapid positive selection of stable integrants following transfection of Plasmodium falciparum 
 Mol Biochem Parasitol 2002 123 1 10 12165384 
Wellems TE  Panton LJ  Gluzman IY  do Rosario VE  Gwadz RW    Chloroquine resistance not linked to mdr -like genes in a Plasmodium falciparum  cross Nature 1990 345 253 255 1970614 
Whitfield ML  Sherlock G  Saldanha AJ  Murray JI  Ball CA    Identification of genes periodically expressed in the human cell cycle and their expression in tumors Mol Biol Cell 2002 13 1977 2000 12058064 
Williamson DH  Preiser PR  Moore PW  McCready S  Strath M    The plastid DNA of the malaria parasite Plasmodium falciparum  is replicated by two mechanisms Mol Microbiol 2002 45 533 542 12123462 
Wilson RJ   Progress with parasite plastids J Mol Biol 2002 319 257 274 12051904 
Wilson RJ  Denny PW  Preiser PR  Rangachari K  Roberts K    Complete gene map of the plastid-like DNA of the malaria parasite Plasmodium falciparum 
 J Mol Biol 1996 261 155 172 8757284 
Wu Y  Wang X  Liu X  Wang Y   Data-mining approaches reveal hidden families of proteases in the genome of malaria parasite Genome Res 2003 13 601 616 12671001 
Zuegge J  Ralph S  Schmuker M  McFadden GI  Schneider G   Deciphering apicoplast targeting signals-feature extraction from nuclear-encoded precursors of Plasmodium falciparum  apicoplast proteins Gene 2001 280 19 26 11738814

PMID: 12929206
Accession ID: PMC176546
License: CC BY
Last Updated: 2021-01-05 08:21:06
Retracted: no
Citation: PLoS Biol. 2003 Oct 18; 1(1):e6
==== Front
PLoS BiolPLoS BiolpbioplosbiolPLoS Biology1544-91731545-7885Public Library of Science San Francisco, USA 10.1371/journal.pbio.0000006Research ArticleEcologyEvolutionGenetics/Genomics/Gene TherapyZoologyMammalsDNA Analysis Indicates That Asian Elephants Are Native to Borneo and Are Therefore a High Priority for Conservation Borneo Elephant OriginFernando Prithiviraj pf133@columbia.edu
1

2
Vidya T. N. C 
3
Payne John 
4
Stuewe Michael 
5
Davison Geoffrey 
4
Alfred Raymond J 
4
Andau Patrick 
6
Bosi Edwin 
6
Kilbourn Annelisa 
7
ΔMelnick Don J 
1

2
1Center for Environmental Research and Conservation, Columbia UniversityNew York, New YorkUnited States of America2Department of Ecology, Evolution, and Environmental Biology, Columbia UniversityNew York, New YorkUnited States of America3Center for Ecological Sciences, Indian Institute of ScienceBangaloreIndia4World Wide Fund for Nature–MalaysiaKota Kinabalu, SabahMalaysia5Asian Rhino and Elephant Action Strategy Programme, World Wildlife FundWashington, District of ColumbiaUnited States of America6Sabah Wildlife DepartmentKota Kinabalu, SabahMalaysia7Field Veterinary Program, Wildlife Conservation SocietyBronx, New YorkUnited States of America10 2003 18 8 2003 18 8 2003 1 1 e63 6 2003 29 7 2003 Copyright: ©2003 Fernando et al.2003This is an open-access article distributed under the terms of the Creative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are properly credited.
Borneo Elephants: A High Priority for Conservation 
The origin of Borneo's elephants is controversial. Two competing hypotheses argue that they are either indigenous, tracing back to the Pleistocene, or were introduced, descending from elephants imported in the 16th–18th centuries. Taxonomically, they have either been classified as a unique subspecies or placed under the Indian or Sumatran subspecies. If shown to be a unique indigenous population, this would extend the natural species range of the Asian elephant by 1300 km, and therefore Borneo elephants would have much greater conservation importance than if they were a feral population. We compared DNA of Borneo elephants to that of elephants from across the range of the Asian elephant, using a fragment of mitochondrial DNA, including part of the hypervariable d-loop, and five autosomal microsatellite loci. We find that Borneo's elephants are genetically distinct, with molecular divergence indicative of a Pleistocene colonisation of Borneo and subsequent isolation. We reject the hypothesis that Borneo's elephants were introduced. The genetic divergence of Borneo elephants warrants their recognition as a separate evolutionary significant unit. Thus, interbreeding Borneo elephants with those from other populations would be contraindicated in ex situ conservation, and their genetic distinctiveness makes them one of the highest priority populations for Asian elephant conservation.

Comparison between DNA sequences of Borneo elephants with those of other Asian elephants settles a longstanding dispute about the origins of these endangered animals
==== Body
Introduction
Elephants have a very limited distribution in Borneo, being restricted to approximately 5% of the island in the extreme northeast (Figure 1). There are no historical records of elephants outside of this range. Fossil evidence for the prehistoric presence of elephants on Borneo is limited to a single specimen of a tooth from a cave in Brunei (Hooijer 1972).

Figure 1 Asian Elephant Range and Sampling Locations in Borneo
Solid lines demarcate country borders and the dotted line the boundary between the Malaysian states of Sabah and Sarawak. Black dots indicate areas of sample collection.

Popular belief holds that elephants presented to the Sultan of Sulu in 1750 by the East India Trading Company and subsequently transported to Borneo founded the current population (Harrisson and Harrisson 1971; Medway 1977). These animals presumably originated in India (Shoshani and Eisenberg 1982), where company operations and trade in domesticated elephants were centred. Alternatively, considering the geographic proximity to Borneo, the elephant trade that flourished in Sumatra and peninsular Malaysia during the 16th–18th centuries (Andaya 1979; Marsden 1986[1811]) may have been the source. Thus, if elephants were introduced to Borneo, the source population could have been India, Sumatra, or peninsular Malaysia, and as a feral population, Borneo's elephants would have low conservation importance.

Conversely, if elephants occurred naturally on Borneo, they would have colonised the island during Pleistocene glaciations, when much of the Sunda shelf was exposed (Figure 2) and the western Indo-Malayan archipelago formed a single landmass designated as Sundaland (MacKinnon et al. 1996). Thus, the isolation of Borneo's elephants from other conspecific populations would minimally date from the last glacial maximum, 18,000 years ago, when land bridges last linked the Sunda Islands and the mainland (MacKinnon et al. 1996). If Borneo's elephants are of indigenous origin, this would push the natural range of Asian elephants 1300 km to the east, and as a unique population at an extreme of the species' range, Borneo elephants' in situ conservation would be a priority and ex situ cross-breeding with other populations would be contraindicated.

Figure 2 Asian Elephant Range and Sampling Locations
Central sampling locations denote the countries sampled and represent a number of actual sampling locations within each country. 1. Sri Lanka, 2. India, 3. Bhutan, 4. Bangladesh, 5. Thailand, 6. Laos, 7. Vietnam, 8. Cambodia, 9. Peninsular Malaysia, 10. Sumatra (Indonesia) 11. Borneo (Sabah–Malaysia).

Initially, Borneo elephants were classified as a unique subspecies (Elephas maximus borneensis) based on morphological differences from other populations (Deraniyagala 1950, 1955). Subsequently, they were subsumed under the Indian Elephas maximus indicus (Shoshani and Eisenberg 1982) or the Sumatran Elephas maximus sumatrensis (Medway 1977) subspecies, based on an assumption of their introduction to the region or on the reasoning that morphological divergence was insufficient to warrant separate status. While unique subspecific status would highlight their conservation importance, evaluation of their status in terms of evolutionary significant units (ESUs) and management units (MUs) (Ryder 1986; Moritz 1994) would be more relevant to conservation management.

Results
We PCR-amplified and sequenced a 630 bp fragment of mitochondrial DNA (mtDNA), including the hypervariable left domain of the d-loop (Fernando et al. 2000), from 20 Borneo elephants and compared them with 317 sequences we generated for elephants across ten of the 13 Asian elephant range states (Figure 2). Asian elephant haplotypes segregated into two distinct clades, α and β (Fernando et al. 2000). All ‘Sundaland’ (peninsular Malaysia, Sumatra, and Borneo) haplotypes fell in clade β, while α and β clades were observed in Sri Lanka and mainland populations (Figures 3 and 4). The Borneo population was fixed for the unique β-haplotype BD. Similar tree topologies were obtained by maximum parsimony, neighbour joining, and maximum-likelihood methods of phylogenetic analyses, with some minor rearrangements of the terminal branches. In all trees, Bornean and other haplotypes unique to ‘Sundaland' (Borneo: BD; peninsular Malaysia: BQ, BV; Sumatra: BS, BU, BT, BR) occupied basal positions in the β-clade phylogeny (Figure 3) and were derived from internal nodes in a parsimony network of haplotypes (Figure 4). Uncorrected p distances between the Borneo haplotype and other β-haplotypes ranged from 0.012 (haplotypes BQ, BP, BO, BS, BU) to 0.020 (haplotype BE), with a mean of 0.014. Assuming a nucleotide substitution rate of 3.5% per million years for the elephant mtDNA d-loop (Fleischer et al. 2001), the observed genetic distance indicates divergence of the Borneo haplotype BD and its closest relative from a common ancestor approximately 300,000 years ago. Owing to stochastic coalescent processes, the use of a single gene to infer population parameters is prone to error. Despite any such error, the magnitude of the genetic difference between Borneo and other Asian elephant haplotypes is such that it indisputably excludes divergence since introduction; the observed divergence is so great that even if there was some error it would not have any influence on the conclusion that places the Borneo haplotype in a timeframe supporting a Pleistocene colonisation rather than introduction by humans.

Figure 3 A Neighbour-Joining Phylogram of Asian Elephant Haplotypes Rooted with an African Elephant Out-Group
Sunda Region haplotypes are in bold.

Figure 4 Network of Asian Elephant Haplotypes Based on Statistical Parsimony
Grey circles with letters denote haplotypes unique to the Sunda region (BD: Borneo; BQ, BV: peninsular Malaysia; BR, BS, BT, BU: Sumatra). White circles with letters denote haplotypes found in mainland Asia (excluding peninsular Malaysia) and Sri Lanka. The small open circles denote hypothetical haplotypes. Haplotypes beginning with the letters A and B belong to the two clades α and β, respectively.

We also genotyped 15 Borneo elephants for five polymorphic autosomal microsatellite loci (Nyakaana and Arctander 1998; Fernando et al. 2001) and compared them to 136 five-locus genotypes we generated for Asian elephants from nine range states. Tests of Hardy–Weinberg equilibrium and linkage disequilibrium in all populations indicated simple Mendelian inheritance of five unlinked, selectively neutral loci. The total number of alleles per locus across populations in the Asian elephant ranged from 2.0 (EMX-2) to 11.0 (LafMS03) (x¯, SE = 4.60, 1.51); the average number of alleles across loci, per population (excluding Borneo), from 2.0 (Sumatra) to 3.6 (Sri Lanka) (x¯, SE = 2.93, 0.155); the observed heterozygosity H0 across all populations (excluding Borneo) from 0.38 (EMX-4) to 0.63 (LafMS03) (x¯, SE = 0.44, 0.041); and gene diversity from 0.39 (EMX-4) to 0.69 (LafMS03) (x¯, SE = 0.47, 0.050). Comparatively, all indices demonstrated very low genetic diversity in the Borneo population: proportion of polymorphic loci, 0.4; number of alleles per locus, 1–2 (x¯, SE = 1.40, 0.219); gene diversity, 0–0.13 (x¯, SE = 0.04, 0.024); heterozygosity H0 = 0–0.07 (x¯, SE = 0.01, 0.013). The number of alleles, observed heterozygosity, and gene diversity, averaged across Asian elephant populations, were all higher than those in Borneo, at all loci (Table 1). Similarly, in all populations, the number of alleles and observed heterozygosity, averaged across loci, were higher than in Borneo (Table 2). Five unique genotypes were identified in the 15 Borneo elephants sampled. In tests of population subdivision, all pairwise comparisons between Borneo and other populations demonstrated highly significant differentiation, FST 0.32–0.63 (x¯, SE = 0.44, 0.034) (Table 3). In tests of a recent bottleneck, no heterozygote excess (Maruyama and Fuerst 1985) or mode-shift distortion of allele frequency distributions (Luikart et al. 1998a), characteristic of a recent bottleneck, was observed in the Borneo population. In assignment tests indicating the distinctness of a population's genotypes, all five Borneo genotypes were assigned with maximum likelihood to Borneo (likelihoods ranging from 0.004 to 0.80, x¯, SE = 0.51, 0.175), and maximum-likelihood ratios of the most-likely (Borneo) to the next-most-likely population ranged from 2.97 to 48.20 (x¯, SE = 25.02, 8.795). Borneo was significantly more likely to be the source than any other population for all five genotypes, since each of the assignment likelihoods to Borneo fell outside the upper end of the corresponding distribution of assignment likelihoods to the other populations. Assignment likelihoods to the putative Indian, Sumatran, and peninsular Malaysian source populations were very small (India: 0–0.0004, x¯, SE = 0.000126, 0.000065; Sumatra: 0–0.0355, x¯, SE = 0.007146, 0.006336; peninsular Malaysia: 0.0003–0.1195, x¯, SE = 0.0301, 0.0201), indicating that Borneo's genotypes were highly unlikely to have originated from any of these populations.

Table 1 Comparison of Measures of Genetic Variation at Individual Loci in Borneo with Those of the Other Populations
Table 2 Measures of Genetic Variation Using Five Loci, in Asian Elephant Populations from across the Range
Table 3 FST Values in Pairwise Comparison of Borneo with Other Populations
Discussion
mtDNA evidence supports an indigenous hypothesis in three ways. First, this hypothesis assumes an ancient, independent evolution of Borneo's elephants, resulting in the unique, divergent Borneo haplotype(s), as we observed. Conversely, the introduction hypothesis assumes an introduction at 500 years ago or less, which approximates zero time on a scale of mtDNA d-loop evolution, and hence requires Borneo and source population haplotypes to be identical. This was not observed. Second, the estimated divergence time between the Borneo haplotype and other Asian elephant haplotypes is concordant with a mid- to late-Pleistocene isolation of elephants on Borneo and the vicariant history of the island (MacKinnon et al. 1996). Third, all observed ‘Sundaland' haplotypes, including Borneo's, were of the β clade, had basal relationships to that clade in a phylogenetic tree, and were independently derived from internal nodes in a haplotype network, suggesting an ancient isolation of these lineages on Borneo, Sumatra, and peninsular Malaysia. Thus, the Borneo haplotype fits a pattern of distribution and relatedness to other ‘Sundaland' haplotypes that is congruent with an ancient colonisation of the Sunda region by β clade and subsequent allopatric divergence of populations on its larger landmasses.

Microsatellite data also support the indigenous hypothesis. If the Borneo population originated from animals introduced in the 16th–18th centuries, it would have reached its mid-20th-century size of approximately 2,000 individuals (deSilva 1968) in fewer than 30 generations, assuming an Asian elephant generation time of 15–20 years (Sukumar 1989). Thus, the Borneo population would have experienced a rapid demographic expansion after the ‘recent’ bottleneck caused by the founder-event of introduction. We did not observe a heterozygote excess or a mode-shift distortion in allele frequency distribution in the Borneo population, suggesting that the population did not undergo a recent bottleneck and hence did not arise from a few introduced animals. However, this result by itself is not conclusive, since with a sample size of 15 and five loci, the test for heterozygosity excess has low power and bottlenecks may not be detected (Luikart et al. 1998b). We observed extremely low genetic diversity at Borneo elephant microsatellite loci, including fixation at three of the five loci. Sequential founder-events or persistent small population size, as would be expected in a small population isolated since the Pleistocene, would lead to substantial loss of genetic variation (Nei et al. 1975) and hence is consistent with the data. Successful founding of a population by a very few individuals from a single introduction could also result in a severe bottleneck. However, given the adversities faced by translocated elephants (Fernando 1997) and the importance of social structure in the reproduction and survival of elephants (Fernando and Lande 2000; McComb et al. 2001), such an explanation is unlikely.

In the assignment tests, all five Borneo genotypes, which included free-ranging as well as captive animals, were assigned to Borneo with significantly higher likelihoods than to other populations and with extremely low likelihoods to the putative source populations. An introduced population may be highly divergent from the source population in terms of F statistics (Williams et al. 2002) due to allelic loss from founder-events. However, the probability of loss for a particular allele is inversely proportional to its frequency in the founder and hence the source population. Thus, genotypes in an introduced population would retain a high likelihood of assignment to the source population, enabling its identification from among a number of candidate populations. Therefore, the assignment tests strongly suggest that the Borneo elephants were not derived from another population in the recent past.

Thus, microsatellite data strongly suggest a Pleistocene colonisation, independent evolution through a long period of isolation, and long-term small population size for the Borneo population. It strongly rejects a recent origin from any of the putative source populations.

Mitochondrial and microsatellite analyses indicate that Borneo's elephants are indigenous to Borneo, have undergone independent evolution since a Pleistocene colonisation, and are not descended from animals introduced by humans. The evolutionary history of Borneo's elephants warrants their recognition as a separate ESU (Moritz 1994). Thus, they should not be cross-bred with other Asian elephants in ex situ management. The genetic distinctiveness and evolutionary history of Borneo elephants support their recognition as a unique subspecies. However, one of the reasons E. maximus borneensis was subsumed under E. m. indicus and E. m. sumatrensis was the inadequacy of the original description of E. m. borneensis in terms of the morphological characters assessed and sample size. Therefore, we suggest that a formal reinstatement of the E. m. borneensis taxa await a detailed morphological analysis of Borneo elephants and their comparison with other populations.

While Borneo's elephants appear to be genetically depauperate, through a long history of isolation and inbreeding, they may have purged deleterious recessive alleles from their genome and decreased their genetic load, thus becoming less susceptible to inbreeding depression. We recommend research on reproductive rates, juvenile survival, and other indicators of detrimental effects of inbreeding such as sperm deformities, sperm mobility, and genetic diversity at MHC loci. While increasing genetic diversity by introducing a small number of elephants from other populations (Whitehouse and Harley 2001) may have to be considered if deleterious inbreeding effects are evident, in the absence of such findings Borneo's elephants should be managed separately from other Asian elephants.

Materials and Methods

Samples.
Samples consisted of dung from free-ranging and dung or blood from captive elephants. Sample collection, storage, and DNA extraction followed published protocols (Fernando et al. 2000, 2003). For mitochondrial and microsatellite analysis, respectively, 20 and 15 samples from Borneo (nine blood samples from elephants captured for management purposes—eight from the Kretam area and one individual originating from around Lahad Datu—and the rest from dung samples from free-ranging elephants collected during a survey of the Kinabatangan watershed) were compared with 317 and 136 samples from across the current Asian elephant range, Sri Lanka (n = 81, 20), India (n = 81, 20), Bhutan (n = 13, 13), Bangladesh (n = 30, 20), Thailand (n = 8, 8), Cambodia (n = 30, 20), Vietnam (n = 5, 0), Laos (n = 20, 6), Indonesia (Sumatra) (n = 40, 20), and peninsular Malaysia (n = 9, 9). Vietnam was excluded from the microsatellite analysis owing to nonamplification of a number of samples.

mtDNA amplification and sequencing.
Approximately 630 bp of mtDNA, including the left domain of the d-loop, were amplified using published primers (Fernando et al. 2000). PCR products were sequenced in both directions, using internal sequencing primers MDLseq-1 (CCTACAYCATTATYGGCCAAA) and MDLseq-2 (AGAAGAGGGACACGAAGATGG), and resolved in 4% polyacrylamide gels in an ABI 377 automated sequencer (Perkin-Elmer, Wellesley, Massachusetts, United States).

mtDNA phylogenetic analysis.
We used 600 bp of the amplified segment in the analysis. Sequences were aligned and edited using SEQUENCHER version 3.1.1 (GeneCodes Corporation, Ann Arbor, Michigan, United States). Sequences were deposited in GenBank (accession numbers AY245538 and AY245802 to AY245827). Phylogenetic analyses were conducted using PAUP* version 4.0 (Swofford 1998). Three African elephant (Loxodonta africana) sequences from zoo animals in the United States were used as an out-group. Genetic distances among sequences were calculated using uncorrected p distances. Maximum-parsimony analysis was conducted using a heuristic search with random stepwise addition of taxa, tree bisection/reconnection branch swapping, and equal weighting; neighbour joining, with Kimura two-parameter distances; and maximum likelihood, using empirical base frequencies and estimated values for the shape parameter for among-site rate variation and transition/transversion ratios. A network of haplotypes was created using statistical parsimony in the software TCS version 1.13 (Clement et al. 2001).

Microsatellite amplification.
Samples were screened with five published microsatellite loci, EMX-1 to EMX-4 (Fernando et al. 2001) and LafMS03 (Nyakaana and Arctander 1998). Forward primers were fluorescent labelled (FAM, HEX, or TET), samples were amplified in 12.5 μl volumes with relevant cycling profiles (Fernando et al. 2001), and 1 μl of PCR product was mixed with 0.2 μl of loading-dye and 0.5 μl of Tamra 500 size standard (Applied Biosystems, Foster City, California, United States) and was resolved in 4% polyacrylamide gels in an ABI 377 automated sequencer. Alleles were scored using GENESCAN software (Applied Biosystems) and published guidelines (Fernando et al. 2003).

Microsatellite data analysis.
Deviations from Hardy–Weinberg equilibrium for each locus and population were tested using the exact Hardy–Weinberg test as implemented in GENEPOP 3.2 (Raymond and Rousset 1995), with the complete enumeration method (Louis and Dempster 1987) for loci with fewer than four alleles and with the Markov chain method (Guo and Thompson 1992) (dememorization: 1000; batches: 100; iterations per batch: 1000) for loci with more than four alleles. GENEPOP was also used to test for linkage disequilibrium between loci, using the Markov chain method. Population differentiation was tested with estimates of Wright's fixation index (Weir and Cockerham 1984), FST, using the program Arlequin version 2 (Schneider et al. 2000).

Evidence for a recent bottleneck in the Borneo population in terms of a heterozygote excess (Cornuet and Luikart 1996) or a mode-shift distortion in allele frequencies (Luikart et al. 1998a) was conducted using the program BOTTLENECK version 1.2.02 (Piry et al. 1997) and a graphical method (Luikart et al. 1998a).

Assignment tests were performed using WHICHRUN version 4.1 (Banks and Eichert 2000). Assuming Hardy–Weinberg equilibrium in each baseline population and linkage equilibrium between loci, the likelihood that an individual originates from a particular population is the Hardy–Weinberg frequency of the individual's genotype at that locus, in that population. This likelihood was multiplied across loci to obtain a multilocus assignment likelihood of the test individual to each population, and the population with the highest value was identified as the ‘most-likely’ source population. To test for statistical significance of the most-likely source population, this assignment likelihood was compared with the distribution of assignment likelihoods of the other populations. Maximum-likelihood ratios were calculated as the ratio between the likelihood of assignment to the most-likely population to that for a particular population.

Supporting Information

Accession Numbers
The GenBank accession numbers for the sequences reported in this paper are AY245538 and AY245802 to AY245827.

We would like to thank Susan Mikota, Peter Malim, Eric Wickramakayake, Richard Lair, Jayantha Jayewardene, L. K. A. Jayasinghe, Manori Gunawardene, H. K. Janaka, Chandana Rajapakse, Ashoka Dangolla, Raman Sukumar, Ajay Desai, Christy Williams, Ainun Nishat, Mohsinuzzman Chowdhury, Mike Keele, Jeff Briscoe, Steve Osofsky, Karl Stromayer, Andrew Maxwell, Ou Ratanak, Lic Vuthy, Joe Heffernen, Rob Tizard, Tom Dillon, Vongphet, Buntjome, Kari Johnson, Heidi Riddle, Simon Hedges, Martin Tyson, Joshua Ginsberg, the Sabah Wildlife Department, Fauna and Flora International, the Department of Wildlife Conservation Sri Lanka, the International Union for Conservation of Nature and Natural Resources Bangladesh, the Zoological Gardens and Wildlife Rescue Centre Cambodia, Angkor Village Resort Elephant Farm (Siem Reap, Cambodia), the Seblat Elephant Training Centre (Bengkulu, Sumatra), Have Trunk Will Travel, the Department of Forests and Wildlife Cambodia, the Wildlife Trust, the World Wildlife Fund (WWF) Malaysia, WWF Vietnam, the Wildlife Conservation Society, the Portland (Oregon) Zoo, the Los Angeles Zoo, the Singapore Zoo, and the Pinnawela Elephant Orphanage Sri Lanka for help in obtaining samples; and Jennifer Pastorini, Ajay Desai, and two anonymous reviewers for comments on an earlier version of the manuscript. This study was conducted in partnership with the WWF's Asian Rhino and Elephant Action Strategy (AREAS) Programme and through additional collaboration with Wildlife Trust's Indian and Sri Lankan Elephant Programs and the Wildlife Conservation Society's Indonesia–Sumatran Elephant Project and Field Veterinary Program. It was made possible by grants from Ms. Nancy Abraham, the WWF United States, WWF for Nature (WWF International), the United States Fish and Wildlife Service's Asian Elephant Conservation Fund, and the Center for Environmental Research and Conservation Seed Grant Program and by additional support from the Laboratory of Genetic Investigation and Conservation, Columbia University. We dedicate this paper to the memory of our coauthor Annelisa Kilbourn, whose untimely death during her work in Gabon is a great loss to conservation.


Conflicts of Interest. The authors have declared that no conflicts of interest exist.


Author Contributions. This project is part of an ongoing multicentre collaboration on elephant conservation. All authors on this manuscript contributed substantively to the work described herein.

Academic Editor: Craig Moritz, University of California, Berkeley.

Δ In the online version of this article published on August 18, Annelisa Kilbourn's affiliation was incorrectly identified as the Sabah Wildlife Department. Her proper affiliation is shown here.

Abbreviations
ESUevolutionary significant unit

mtDNAmitochondrial DNA

MUmanagement unit.
==== Refs
References
Andaya B   Perak, the abode of grace: A study of an eighteenth-century Malay state 1979 Kuala Lumpur Oxford University Press 462 
Banks MA  Eichert W   WHICHRUN (version 3.2): A computer program for population assignment of individuals based on multilocus genotype data J Hered 2000 91 87 89 10739137 
Clement M  Derington J  Posada D   TCS: Estimating gene genealogies. Version 1.13 2001 Provo (Utah) Brigham Young University 
Cornuet JM  Luikart G   Description and power analysis of two tests for detecting recent population bottlenecks from allele frequency data Genetics 1996 144 2001 2014 8978083 
Deraniyagala PEP   The elephant of Asia Proc Ceylon Assoc Sci 1950 3 1 18 
Deraniyagala PEP   Some extinct elephants, their relatives, and the two living species 1955 Colombo, Ceylon Government Press 161 
deSilva GS   Elephants of Sabah J Sabah Soc 1968 3 169 181 
Fernando P   Keeping jumbo afloat: Is translocation an answer to the human–elephant conflict? Sri Lanka Nature 1997 1 4 12 
Fernando P  Lande R   Molecular genetic and behavioral analyses of social organization in the Asian elephant Behav Ecol Sociobiol 2000 48 84 91 
Fernando P  Pfrender ME  Encalada S  Lande R   Mitochondrial DNA variation, phylogeography, and population structure of the Asian elephant Heredity 2000 84 362 372 10762406 
Fernando P  Vidya TNC  Melnick DJ   Isolation and characterisation of tri- and tetranucleotide microsatellite loci in the Asian elephant, Elephas maximus 
 Mol Ecol Notes 2001 1 232 233 
Fernando P  Vidya TNC  Rajapakse C  Dangolla A  Melnick DJ   Reliable non-invasive genotyping: Fantasy or reality? J Hered 2003 94 115 123 12721223 
Fleischer RC  Perry EA  Muralidharan K  Stevens EE  Wemmer CM   Phylogeography of the Asian elephant (Elephas maximus ) based on mitochondrial DNA Evolution 2001 55 1882 1892 11681743 
Guo SW  Thompson EA   Performing the exact test of Hardy–Weinberg proportions for multiple alleles Biometrics 1992 48 361 372 1637966 
Harrisson T  Harrisson B   The prehistory of Sabah Sabah Soc J Monogr 1971 4 1 272 
Hooijer DA   Prehistoric evidence for Elephas maximus  L. in Borneo Nature 1972 239 228 
Louis EJ  Dempster ER   An exact test for Hardy–Weinberg and multiple alleles Biometrics 1987 43 805 811 3427165 
Luikart G  Allendorf FW  Cornuet JM  Sherwin WB   Distortion of allele frequency distributions provides a test for recent population bottlenecks J Hered 1998a 89 238 247 9656466 
Luikart G  Sherwin WB  Steele BM  Allendorf FW   Usefulness of molecular markers for detecting population bottlenecks via monitoring genetic change Mol Ecol 1998b 7 963 974 9711862 
MacKinnon K  Hatta G  Halim H  Mangalik A   The ecology of Kalimantan 1996 Hong Kong Periplus Editions Ltd 802 
Marsden W   The history of Sumatra 1986 [1811] Kuala Lumpur Oxford University Press 532 
Maruyama T  Fuerst PA   Population bottlenecks and non-equilibrium models in population genetics. II. Number of alleles in a small population that was formed by a recent bottleneck Genetics 1985 111 675 689 4054612 
McComb K  Moss C  Durant SM  Baker L  Sayialel S   Matriarchs as repositories of social knowledge in African elephants Science 2001 292 491 494 11313492 
Medway L   Mammals of Borneo Monogr Malay Br R Asia Soc 1977 7 1 172 
Moritz C   Defining ‘evolutionary significant units' for conservation Trends Ecol Evol 1994 9 373 375 21236896 
Nei M  Maruyama T  Chakraborty R   The bottleneck effect and genetic variability in populations Evolution 1975 29 1 10 
Nyakaana S  Arctander P   Isolation and characterisation of microsatellite loci in the African elephant (Loxodonta africana  Blumenbach 1797) Mol Ecol 1998 7 1436 1437 9787454 
Piry S  Luikart G  Cornuet JM   BOTTLENECK: A program for detecting recent effective population size reductions from allele frequency data 1997 Laboratoire de Modelisation et Biologie Evolutive, Montpellier, France 
Raymond M  Rousset F   GENEPOP (version 1.2): Population genetics software for exact tests and ecumenicism J Hered 1995 86 248 249 
Ryder OA   Species conservation and systematics: The dilemma of subspecies Trends Ecol Evol 1986 1 9 10 
Schneider S  Roessli D  Excoffier L   Arlequin: A software for population genetics data analysis. Version 2.000 2000 Geneva Genetics and Biometry Laboratory, University of Geneva 
Shoshani J  Eisenberg JF   
Elephas maximus 
 Mamm Sp 1982 182 1 8 
Sukumar R   The Asian elephant: Ecology and management 1989 Cambridge Cambridge University Press 272 
Swofford DL   PAUP*: Phylogenetic analysis using parsimony (and other methods). Version 4 1998 Sunderland, Massachusetts Sinauer Associates 
Weir BS  Cockerham CC   Estimating F -statistics for the analysis of population structure Evolution 1984 38 1358 1370 
Whitehouse AM  Harley EH   Post-bottleneck genetic diversity of elephant populations in South Africa, revealed using microsatellite analysis Mol Ecol 2001 10 2139 2149 11555257 
Williams CL  Serfass TL  Cogan R  Rhodes OE   Microsatellite variation in the reintroduced Pennsylvania elk herd Mol Ecol 2002 11 1299 1310 12144652

PMID: 0
Accession ID: PMC176547
License: CC BY
Last Updated: 2021-01-05 08:21:06
Retracted: no
Citation: PLoS Biol. 2003 Oct 18; 1(1):e7
==== Front
PLoS BiolPLoS BiolpbioplosbiolPLoS Biology1544-91731545-7885Public Library of Science San Francisco, USA 10.1371/journal.pbio.0000007SynopsisEcologyEvolutionGenetics/Genomics/Gene TherapyZoologyMammalsBorneo Elephants: A High Priority for Conservation Synopsis10 2003 18 8 2003 18 8 2003 1 1 e7Copyright: © 2003 Public Library of Science.2003This is an open-access article distributed under the terms of the Creative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are properly credited.
DNA Analysis Indicates That Asian Elephants Are Native to Borneo and Are Therefore a High Priority for Conservation
==== Body
A new study settles a long-standing dispute about the genesis of an endangered species. With scant fossil evidence supporting a prehistoric presence, scientists could not say for sure where Borneo's elephants came from. Did they descend from ancient prototypes of the Pleistocene era or from modern relatives introduced just 300–500 years ago? That question, as Fernando et al. report in this issue, is no longer subject to debate.

Applying DNA analysis and dating techniques to investigate the elephants' evolutionary path, researchers from the United States, India, and Malaysia, led by Don Melnick of the Center for Environmental Research and Conservation at Columbia, demonstrate that Borneo's elephants are not recent arrivals. They are genetically distinct from other Asian elephants and may have parted ways with their closest Asian cousins when Borneo separated from the mainland, effectively isolating the Borneo elephants some 300,000 years ago.

In the 1950s, Borneo elephants had been classified as a subspecies of Asian elephants (either Indian or Sumatran) based on anatomical differences, such as smaller skull size and tusk variations. This classification was later changed, partly because of the popular view that these animals had descended from imported domesticated elephants. Until now, there was no solid evidence to refute this belief and no reason to prioritize the conservation of Borneo elephants.

Their new status, as revealed by this study, has profound implications for the fate of Borneo's largest mammals. Wild Asian elephant populations are disappearing as expanding human development disrupts their migration routes, depletes their food sources, and destroys their habitat. Recognizing these elephants as native to Borneo makes their conservation a high priority and gives biologists important clues about how to manage them.

Borneo elephant

PMID: 0
Accession ID: PMC176548
License: CC BY
Last Updated: 2021-01-05 08:21:04
Retracted: no
Citation: PLoS Biol. 2003 Oct 18; 1(1):e11
==== Front
PLoS BiolPLoS BiolpbioplosbiolPLoS Biology1544-91731545-7885Public Library of Science San Francisco, USA 10.1371/journal.pbio.0000011SynopsisGenetics/Genomics/Gene TherapyInfectious DiseasesMicrobiologyPlasmodiumMonitoring Malaria: Genomic Activity of the Parasite in Human Blood Cells Synopsis10 2003 18 8 2003 18 8 2003 1 1 e11Copyright: © 2003 Public Library of Science.2003This is an open-access article distributed under the terms of the Creative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are properly credited.
Microarray Analysis: Genome-Scale Hypothesis Scanning 

The Transcriptome of the Intraerythrocytic Developmental Cycle of Plasmodium falciparum
==== Body
Every year, malaria kills as many as 2.5 million people. Of these deaths, 90% occur in sub-Saharan Africa, and most are children. While four species of the single-celled organism Plasmodium cause malaria, Plasmodium falciparum is the deadliest. Harbored in mosquito saliva, the parasite infects its human host as the mosquito feeds on the victim's blood.

Efforts to control the disease have taken on an increased sense of urgency, as more P. falciparum strains show resistance to antimalarial drugs. To develop new drugs and vaccines that disable the parasite, researchers need a better understanding of the regulatory mechanisms that drive the malarial life cycle. Joseph DeRisi and colleagues now report significant progress toward this goal by providing the first comprehensive molecular analysis of a key phase of the parasite's life cycle.

While P. falciparum is a single-celled eukaryotic (nucleated) organism, it leads a fairly complicated life, assuming one form in the mosquito, another when it invades the human liver, and still another in human red blood cells (erythrocytes). The intraerythrocytic developmental cycle (IDC) is the stage of the P. falciparum lifecycle associated with the clinical symptoms of malaria. Using data from the recently sequenced P. falciparum genome, the researchers have tracked the expression of all of the parasite's genes during the IDC.

The pattern of gene expression (which can be thought of as the internal operating system of the cell) during the IDC is strikingly simple. Its continuous and clock-like progression of gene activation is reminiscent of much simple life forms—such as a virus or phage—while unprecedented for a free living organism. Virus and phage behave like a “just-in-time” assembly line: components are made only as needed, and only in the amount that is needed. In this respect, malaria resembles a glorified virus.

Given the remarkable coupling of the timing of gene activation with gene function, as shown in this paper, this understanding could help identify the biological function of the 60% of genes in P. falciparum that encode proteins of unknown function.


P. falciparum appears to be ultra-streamlined and exquisitely tuned to perform a single job: consume, replicate, and invade. The simple program regulating the life of P. falciparum may hold the key to its downfall as any perturbation of the regulatory program will likely have dire consequences for the parasite. This offers renewed hope for the design of inhibitory drugs targeted at the regulatory machinery that would irreparably foul the parasite's regulatory program, ultimately resulting in its death.

Gene expression profile of P. falciparum

PMID: 12975658
Accession ID: PMC193604
License: CC BY
Last Updated: 2021-01-05 08:21:03
Retracted: no
Citation: PLoS Biol. 2003 Oct 15; 1(1):e13
==== Front
PLoS BiolPLoS BiolpbioplosbiolPLoS Biology1544-91731545-7885Public Library of Science San Francisco, USA 10.1371/journal.pbio.0000013Research ArticleCell BiologyDevelopmentGenetics/Genomics/Gene TherapyMolecular Biology/Structural BiologyNeurosciencePhysiologyDrosophila
Drosophila Free-Running Rhythms Require Intercellular Communication Damping Transcriptional RhythmsPeng Ying 
1

2
Stoleru Dan 
1
Levine Joel D 
1
Hall Jeffrey C 
1
Rosbash Michael rosbash@brandeis.edu
1

2
1Department of Biology, Brandeis UniversityWaltham, MassachusettsUnited States of America2Howard Hughes Medical Institute, Brandeis UniversityWaltham, MassachusettsUnited States of America10 2003 15 9 2003 15 9 2003 1 1 e1320 6 2003 4 8 2003 Copyright: ©2003 Peng et al.2003This is an open-access article distributed under the terms of the Creative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are properly credited.
Biological Clock Depends on Many Parts Working Together 
Robust self-sustained oscillations are a ubiquitous characteristic of circadian rhythms. These include Drosophila locomotor activity rhythms, which persist for weeks in constant darkness (DD). Yet the molecular oscillations that underlie circadian rhythms damp rapidly in many Drosophila tissues. Although much progress has been made in understanding the biochemical and cellular basis of circadian rhythms, the mechanisms that underlie the differences between damped and self-sustaining oscillations remain largely unknown. A small cluster of neurons in adult Drosophila brain, the ventral lateral neurons (LNvs), is essential for self-sustained behavioral rhythms and has been proposed to be the primary pacemaker for locomotor activity rhythms. With an LNv-specific driver, we restricted functional clocks to these neurons and showed that they are not sufficient to drive circadian locomotor activity rhythms. Also contrary to expectation, we found that all brain clock neurons manifest robust circadian oscillations of timeless and cryptochrome RNA for many days in DD. This persistent molecular rhythm requires pigment-dispersing factor (PDF), an LNv-specific neuropeptide, because the molecular oscillations are gradually lost when Pdf01 mutant flies are exposed to free-running conditions. This observation precisely parallels the previously reported effect on behavioral rhythms of the Pdf01 mutant. PDF is likely to affect some clock neurons directly, since the peptide appears to bind to the surface of many clock neurons, including the LNvs themselves. We showed that the brain circadian clock in Drosophila is clearly distinguishable from the eyes and other rapidly damping peripheral tissues, as it sustains robust molecular oscillations in DD. At the same time, different clock neurons are likely to work cooperatively within the brain, because the LNvs alone are insufficient to support the circadian program. Based on the damping results with Pdf01 mutant flies, we propose that LNvs, and specifically the PDF neuropeptide that it synthesizes, are important in coordinating a circadian cellular network within the brain. The cooperative function of this network appears to be necessary for maintaining robust molecular oscillations in DD and is the basis of sustained circadian locomotor activity rhythms.

Circadian rhythms are characterized by robust molecular oscillations, which are shown here to require a brain region-specific neuropeptide, PDF, for maintenance and coordination
==== Body
Introduction
Circadian rhythms of diverse organisms are based on similar intracellular molecular feedback loops (Dunlap 1999; Allada et al. 2001; Panda et al. 2002). Based on this view, it is believed that one or a small number of clock cells are sufficient for self-sustained rhythms (Dunlap 1999). This is despite the complex cellular organizations of many tissues, organisms, and systems (Kaneko and Hall 2000; Schibler and Sassone-Corsi 2002).

In Drosophila, circadian clocks have been identified in a diverse range of cell types throughout the head and the body (Glossop and Hardin 2002; Hall 2003). However, the clocks in different cells are considered nonidentical (Krishnan et al. 2001; Glossop and Hardin 2002; Levine et al. 2002a; Schibler and Sassone-Corsi 2002). In many tissues, molecular oscillations undergo rapid damping without environmental timing cues (Hardin 1994; Plautz et al. 1997; Stanewsky et al. 1997; Giebultowicz et al. 2000). This is similar to the damping of in vitro rhythms in some mammalian tissues (Balsalobre et al. 1998; Schibler and Sassone-Corsi 2002). In contrast, the Drosophila “core pacemaker” is believed to maintain robust oscillations for a long time in constant darkness (DD) with little or no damping, such that circadian behaviors can persist under such conditions (Dowse et al. 1987). Indeed, self-sustaining oscillations are a defining characteristic of true circadian rhythms and are believed to be required of a fully functional rhythmic cell. The differences between the “core pacemaker” and the clock machinery within damping cells or systems are unknown.

The six clusters of approximately 100 clock neurons in the adult Drosophila brain are well characterized (Kaneko and Hall 2000). Recent studies have focused principally on one of these groups, the small ventral lateral neurons (s-LNvs), as the best “core pacemaker” candidate for the following reasons: (1) in the developmental mutant disco, the presence of LNvs correlates with the maintenance of behavior rhythmicity (Helfrich-Förster 1997); (2) LNvs specifically express the neuropeptide pigment-dispersing factor (PDF), and the Pdf01-null mutant loses behavioral rhythmicity under DD conditions (Renn et al. 1999); (3) genetic ablation of the LNvs by expressing proapoptotic genes causes the loss of rhythmicity in DD (Renn et al. 1999); and (4) the s-LNvs maintain robust molecular oscillations for at least for 2 days in DD (Yang and Sehgal 2001; Shafer et al. 2002), in contrast to at least some other brain neurons and nonneuronal tissues. This final property suggests that these cells might fulfill the self-sustaining criterion for the “core pacemaker.” Indeed, the s-LNvs have been proposed to the primary pacemaker cells that generate locomotor activity rhythms (Helfrich-Förster 1997; Renn et al. 1999; Emery et al. 2000). Consistent with this cell-autonomous view of circadian rhythmicity, it has been shown that the LNvs possess all components of a fully functional, independent circadian clock: the photoreceptor cryptochrome, the rhythm-generating feedback loops, and a putative output factor, the neuropeptide PDF (Emery et al. 2000). Our pursuit of the self-sustaining “core pacemaker” of the Drosophila circadian system began with a test of the s-LNv cell-autonomous clock hypothesis.

Results
LNvs Cannot Support Circadian Behavior Independently
To test whether the LNvs can support free-running circadian locomotor activity rhythms independently of other functional clock cells, we restricted pacemaker activity to these few PDF-expressing cells. CYCLE (CYC) is a bHLH–PAS protein (Rutila et al. 1998) and forms a heterodimeric transcription factor with CLOCK (CLK), another bHLH–PAS protein (Allada et al. 1998). CYC is an essential component of the Drosophila circadian oscillator transcriptional feedback loop (Glossop et al. 1999). The cyc01 nonsense mutation completely eliminates molecular oscillations, and the direct target genes period (per) and timeless (tim) mRNAs are essentially undetectable (Rutila et al. 1998). Behavioral rhythms are also absent in the cyc01 homozygous mutant strain (Rutila et al. 1998). We rescued cyc01 specifically in the LNvs, by using a well-characterized pdf–GAL4 driver (Renn et al. 1999) in combination with a UAS–CYC transgene to express ectopically wild-type CYC. Since CYC is apparently not a rate-limiting component of active dCLK–CYC complexes (Bae et al. 2000) and does not undergo molecular oscillations itself (Rutila et al. 1998), we expected that CYC overexpression would not cause circadian oscillator dysfunction. Indeed, the presence of the two transgenes did not affect locomotor activity rhythms in a wild-type background (Figure 1C, right panel).

Figure 1 Rescuing Molecular Oscillations within the LNvs Is Not Sufficient to Rescue Locomotor Activity Rhythms
The rescued mutant genotype is y w;pdf–GAL4;UAS–CYC,cyc01/cyc01. The flies were entrained in standard LD conditions and timepoints taken. Molecular oscillations were examined by whole-mount in situ hybridization of the tim gene. Double staining with a Pdf probe was used to label the LNvs neuronal group.

(A and B) These show representative duplicate experiments. No tim mRNA signal is detectable in the dorsal region of the brain. The lower arrows point to the s-LNvs and the upper arrows to the l-LNvs. (A) Brain taken at timepoint ZT3. Panels shown from left to right are Pdf (green, FITC labeled), tim (red, Cy3 labeled), and an image overlay. (B) Brain taken at timepoint ZT15. Panels shown from left to right are Pdf (green, FITC labeled), tim (red, Cy3 labeled), and an image overlay.

(C) The double-plotted actograms of rescue mutant and control flies in a standard LD:DD behavior assay. The colors on the background indicate the lighting conditions of the behavior monitors (white, lights on; light blue, lights off). In the actogram, the average locomotor activity of the group of flies is plotted as a function of time. The left panel shows the actogram of the rescued mutant flies (y w;pdf–GAL4/+;UAS–CYC,cyc01/cyc01, n = 30). RI (rhythm index; Levine et al. 2002a) = 0.14. The right panel shows the actogram for the rescued wild-type (control) flies (y w;pdf–GAL4/+;UAS–CYC/+, n = 32, RI = 0.61).

The rescued mutant flies (pdf–GAL4;UAS–CYC,cyc01/cyc01) were examined by two independent criteria. First, molecular oscillations were assayed by in situ hybridization with a tim probe (Figure 1A and 1B). tim RNA levels undergo robust cycling in wild-type flies, with a trough at ZT3 and a peak at ZT15 (Sehgal et al. 1994). This is also true within all individual clock neurons (Zhao et al. 2003). tim mRNA cycled in the LNvs (Figure 1A and B), indicating successful rescue of the molecular oscillator within these cells. The fact that other clock neurons were still tim mRNA-negative (Figure 1A and B) suggests that CYC and the rest of the molecular machinery can function cell autonomously, at least in the LNvs under these light–dark (LD) conditions. The observed oscillations are also not passively driven by light, since they persisted in DD, at least in the s-LNvs (Figure S1). Second, locomotor activity rhythms were examined by standard behavioral criteria. The transgenic flies were completely arrhythmic in DD. They were also arrhythmic under LD conditions, as the flies failed to anticipate the discontinuous transitions from light to dark or from dark to light (see Figure 1C, left panel; Rutila et al. 1998). In summary, the behavioral phenotypes were indistinguishable from those of the parental cyc01 mutant strain.

Brain Clock Neurons Manifest Robust Molecular Oscillations in DD
The insufficiency of LNv molecular rhythmicity indicates that one or more additional groups of rhythmic clock neurons are required for behavioral rhythmicity. We considered that robust molecular cycling under extended constant darkness conditions might be a good criterion for identifying these cell groups, because prior biochemical studies showed that some head and brain locations undergo damping of molecular oscillations under free-running conditions (Hardin 1994; Stanewsky et al. 1997). This conclusion has been extended by more recent immunohistochemical observations (Yang and Sehgal 2001; Shafer et al. 2002). The criterion of maintaining persistent and robust molecular rhythms in DD therefore suggests that only a limited set of brain locations are likely to be free-running pacemaker candidates. In order to identify these neurons, we assayed fly brains by tim in situ hybridization after 8 days in DD. To our surprise, we found that all tim-expressing brain cell groups (including both large ventral lateral neurons [l-LNvs] and small ventral lateral neurons [s-LNvs], doral lateral neurons [LNds], and all three groups of dorsal neurons [DNs]) still cycle robustly at this time (Figure 2). Previous studies have reported that the l-LNvs fail to maintain oscillations at the beginning of DD (Yang and Sehgal 2001; Shafer et al. 2002). We have reproduced these observations, but noticed that the l-LNvs “adapt” to constant conditions by becoming rhythmic once again after about 2 days in DD (data not shown). These results clearly distinguish the brain from the eyes and other peripheral tissues, which rapidly lose coherent molecular oscillations under free-running conditions (Hardin 1994; Plautz et al. 1997; Stanewsky et al. 1997; Giebultowicz et al. 2000). Although this approach failed to identify the additional neuronal groups necessary for behavioral rhythms, it suggests that many of these brain neuronal groups might act together in a network to support robust rhythms.

Figure 2 All Brain Clock Neuronal Groups Maintain Robust Oscillations of tim RNA Levels in DD
Wild-type flies were entrained for at least 3 days and then released into DD. tim RNA was assayed at trough (left panels) and peak (right panels) timepoints by whole-mount in situ hybridization. Wild-type flies in LD (A) were compared with the eighth day of DD (B). On the eighth day of DD, the locomotor activities of the fly population were still in close synchrony, without any obvious phase spreading (data not shown). Left panels, brains at ZT3 (A) or CT3 (B); right panels, brains from ZT15 (A) or CT15 (B). Both (A) and (B) are representative of three replicate experiments.

Sustained Molecular Oscillation in Constant Darkness Requires PDF
This association between robust molecular oscillations in all brain clock cells and behavioral rhythms in DD also made us consider the role of the neuropeptide PDF. The Pdf01 mutant strain is unique among identified Drosophila circadian mutants, as it has little effect under LD conditions, but loses behavioral rhythmicity gradually and specifically in DD (Renn et al. 1999). This phenotype might reflect a disassociation between behavioral rhythmicity and the underlying molecular oscillations, as predicted from the role of PDF as a circadian output signal; it is proposed to connect the molecular oscillation in the LNvs to locomotor activity (Renn et al. 1999).

We considered a completely different interpretation, namely, that PDF contributes to the functional integration of several brain clock neuronal groups, which is necessary to sustain molecular as well as behavioral rhythmicity under constant conditions. This fits well with previous studies of PDF in other organisms (Rao and Riehm 1993; Petri and Stengl 1997). In contrast to the canonical output model, this possibility suggests that the Pdf01 mutant might manifest unusual molecular oscillations within clock neurons, especially under DD conditions. To address this issue experimentally, we examined Pdf01 mutant flies by tim in situ hybridization.

In Pdf01 flies, all clock neurons had robust tim RNA oscillations in LD, and the cycling phase and amplitude were comparable to those of wide-type flies (Figure 3A). The mutant flies were then released into DD and assayed at various times thereafter. In the first day of DD, cycling was similar to that observed in LD (Figure 3B). By the fourth day of DD, however, the cycling amplitude was much reduced in all clock neurons (Figure 3C and 3D). This was most evident from the unusually high signal in the CT2 sample; in wild-type flies, no tim signal was detected in any clock neuron at this timepoint (Figure 3C, left panels). There was also a reduced signal strength at the peak time, CT14 (Figure 3C, fourth panel from the left). The result parallels the damping of behavioral rhythms in the Pdf01 mutant strain (Renn et al. 1999).

Figure 3 Molecular Oscillations of tim RNA Damp in DD in the Pdf01 Mutant

tim RNA oscillations were examined in the Pdf01 mutant under both LD (A) and different days in DD ([B] and [C]), by whole-mount in situ hybridization. (A), (B), and (C) are representative images from replicas of three experiments.

(A) The left panel is from ZT3, and the right panel is from ZT15. A normal tim oscillation profile is observed compared to that of wild-type (see Figure 2A).

(B) Brains from the Pdf01 mutant in the first day of DD. Left panel, CT3; right panel, CT15. Oscillations are comparable to those in LD.

(C) Brains taken in the fourth day of DD. Six timepoints were taken throughout the circadian day. The sequence of panels from left to right is CT2, 6, 10, 14, 18, and 20, respectively. Wild-type brains (top row) were assayed in parallel with those from the Pdf01 mutant (bottom row). See text for details.

(D) Quantification of (C). Relative intensities are taken from normalized mean pixel intensities. Different clock neuronal groups were quantified independently and compared between wild-type (blue curves) and Pdf01 mutant (purple curves). The panels from left to right are quantification of tim RNA oscillation in the DNs, in the LNds, and in the LNvs. Reduced cycling amplitude and a significant advanced phase were observed in the fourth day of DD. See text for details.

Despite the gradual fading of locomotor activity rhythms in DD, a significant fraction of Pdf01 mutant flies is still weakly rhythmic after 4 d of DD (Renn et al. 1999). By tracking their locomotor activity phases, we observed that most of them had accumulated an approximately 4-hour phase advance relative to wild-type flies by the fourth day in DD. This is consistent with the measured ca. 23-hour periods of these weakly rhythmic flies (1-hour phase advanced per day for 4 days) as well as their advanced evening activity peak in LD (Renn et al. 1999). Quantitation of the tim in situ hybridization signal showed that there was a comparable one-point (4 h) advance in the peak of tim RNA and also confirmed the reduced cycling amplitude (Figure 3D). In order to eliminate the possibility that the observed damping is caused by the asynchrony of the Pdf01 fly population, locomotor activities were tracked in real time. Individual flies were then removed from the monitors to assay tim RNA levels. Identical damped molecular oscillations were also observed in this case (data not shown). Taken together, the results indicate an excellent quantitative correspondence in phase and amplitude between the tim RNA rhythms and the behavioral rhythms in all clock neurons of the Pdf01 strain.

To extend these observations, we also assayed cryptochrome (cry) mRNA oscillations by in situ hybridization. cry is expressed in a similar clock neuron pattern to tim, but it has a peak expression at ZT2 and a trough at ZT14 (Emery et al. 1998; Zhao et al. 2003). This phase is opposite to that of tim and other CLK–CYC direct target genes and reflects the fact that cry is only indirectly regulated by this heterodimeric transcription factor; CLK–CYC directly regulates the transcription factors PDP1 and VRILLE, which then regulate cry (Cyran et al. 2003; Glossop et al. 2003). Despite these differences between tim and cry, a similar result was obtained for cry in the Pdf01 strain in the fourth day of DD (Figure 4), i.e., a reduced cycling amplitude compared to the fourth day of DD in a wild-type strain. This is suggested by the in situ pictures and is strongly indicated by the quantitation (Figure 4). The correspondence between the tim and cry mRNA patterns indicates that the entire circadian transcriptional program damps in the mutant strain in DD, which underlies the behavioral damping.

Figure 4 
cry RNA Oscillation Amplitude Is Also Reduced by the Fourth Day of DD in the Pdf01 Mutant

cry RNA expression in the brain was examined at the fourth day of DD by whole-mount in situ hybridization using a cry probe. Timepoints were taken every 4 hours throughout the circadian day. The sequence of panels from left to right is CT2, 6, 10, 14, 18, and 20, respectively. Wild-type brains (top row) were analyzed in parallel with those from the Pdf01 mutant (bottom row). Shown are representative images from duplicate experiments. Quantification of cry RNA oscillations in different cell groups is as shown in Figure 3. Ubiquitous damping of the cycling amplitude in the different cell groups was observed in the Pdf01 mutant.

PDF Is Likely to Act upon Clock Neurons Directly
It is noteworthy that the mRNA oscillations damp uniformly in the Pdf01 mutant strain, including the PDF-expressing LNvs (see Figures 3 and 4). Since PDF is a neuropeptide (Rao and Riehm 1993), it is unlikely to exert a direct intracellular effect on the LNv transcriptional machinery. A more conservative interpretation is that PDF maintains intercellular communication between individual LNv neurons (Petri and Stengl 1997) and/or between the LNvs and other cells; the communication is essential for self-sustained molecular rhythms within the LNvs. Although this “feedback” could be quite indirect, the l-LNvs project to the contralateral LNvs through the posterior optic tract. Moreover, the s-LNvs project dorsally to the superior protocerebrum, the location of the DNs. (Helfrich-Förster 1995). These anatomic features suggest that PDF might bind directly to clock neurons.

To test this hypothesis, in vitro biotinylated PDF peptide was incubated with fixed adult brains under near physiological conditions. The bound peptide was then detected in situ with a streptavidin-conjugated enzymatic amplification reaction. The vast majority of the signal localized with numerous cells at the periphery of medulla (Figure 5A). This is exactly where the l-LNvs send large arborizations as their centrifugal projections (Helfrich-Förster 1995). Importantly, signal was also detected coincident with the LNvs (Figure 5B) and likely DN3 clock neurons (Figure 5C) within the superior protocerebrum region, i.e., the bound peptide colocalized with GFP when the brains were from a strain with GFP-labeled clock neurons. Staining intensity was temporally constant; i.e., there was no systematic variation in signal intensity with circadian time. Although we obtained identical results with two differently biotinylated PDF peptides and there was no staining with two other biotinylated control peptides, we had difficulty to compete specifically the signal with nonbiotinylated PDF (see Materials and Methods). Moreover, PDF peptide staining of clock neurons was not reliably detected in every brain, in contrast to optic lobe staining. Nonetheless, we never detected peptide staining of other neurons in the vicinity of the LNvs; i.e., signal in this region of the brain was always coincident with the GFP-labeled LNvs. The peptide staining therefore suggests that PDF acts on the LNvs in an autocrine or paracrine fashion as well as on other clock neurons, but the results do not exclude additional, more indirect modes of action.

Figure 5 A PDF Peptide Binds to Many Cells, Including Several Clock Neuronal Groups
In vitro biontinylated PDF peptide was used to visualize the peptide binding locations (middle panels, with Cy3) in the brain (see Materials and Methods for details). We used membrane-bound GFP (green panels on the left) to label specific circadian neurons as well as their projections (right panels show the overlay of both channels).

(A) The brain is from flies with labeled LNvs (y w,UAS–mCD8iGFP;pdf–GAL4). Numerous cells at the periphery of the medulla have the vast majority of the bound PDF peptide signal within the brain. This region receives widespread dendritic arborizations from the l-LNvs.

(B) Bound PDF peptide was also detected on the surface of LNvs at a lower intensity. LNv cell bodies were labeled using UAS–mCD8iGFP;pdf–GAL4. Since the signal from the Cy3 channel was much weaker than the GFP signal, we reduced the output gain from the GFP channel. Sequential scanning was used to prevent cross-talk between the two channels.

(C) y w,UAS–mCD8iGFP;tim–GAL4/+ flies were used to label all circadian neurons. In the dorsal region shown in this series, the arrow points to a group of DN3 neurons.

Discussion
The strong behavioral phenotype of the Pdf01 mutant strain in DD indicates that PDF makes an important contribution to free-running circadian rhythms. It was, however, unanticipated that the Pdf01 mutant would have an additional effect on transcriptional oscillations within most if not all clock neurons. This observation extends the tight parallel between strong behavioral rhythms and robust transcriptional rhythms and suggests that the behavioral damping is due to the transcriptional damping (Marrus et al. 1996). In contrast to this strong effect of the Pdf01 mutation on free-running rhythms, the molecular as well as behavioral rhythms of these mutant flies are nearly normal under LD conditions. We now interpret this difference to indicate that intercellular communication among different clock cells and neuronal groups is less important when they can independently receive photic information via cryptochrome. This probably serves not only to synchronize clock neurons but also to reinforce and strengthen the molecular oscillation (Emery et al. 1998; Stanewsky et al. 1998).

The damping phenotype includes the LNvs, which have been proposed to be the principal pacemaker neurons in Drosophila (Helfrich-Förster 1997; Renn et al. 1999). Their counterparts in mammals, the suprachiasmatic nucleus (SCN) neurons, can support circadian rhythms independently (e.g., Sujino et al. 2003). However, our data indicate that the LNvs cannot support locomotor activity rhythms without other clock cell groups (see Figure 1). A similar attempt to rescue behavioral rhythms of an arrhythmic Clk mutant also failed (Allada et al. 2003). Although the negative result shown here might be due to developmental defects of the cyc01 mutation (Park et al. 2000), the conclusion fits well with a role for PDF in functional cooperation between individual neuronal groups. Indeed, it appears that PDF secretion comprises much of what the LNvs contribute to rhythms, as the phenotype of flies missing the LNvs is virtually identical to that of the Pdf01 strain (Renn et al. 1999). There is less known about the roles of other clock neurons, although they do have specific wiring properties (Kaneko and Hall 2000) as well as specific sets of gene expression profiles (unpublished data). An additional indication that other clock neurons contribute to locomotor activity rhythms is that LD behavioral rhythms do not require the LNvs (Hardin et al. 1992; Renn et al. 1999). As the Pdf01 strain also has a strong effect on geotaxis (Toma et al. 2002), clock neurons may even contribute to other behavioral modalities.

The staining pattern suggests that the PDF ligand contacts a receptor on the surface of clock neurons, including the LNvs themselves. This is consistent with the notion that PDF acts as an important intercellular cell communication molecule within the Drosophila circadian system. The dorsal projections of the s-LNvs stain rhythmically with anti-PDF antibodies, and it has been suggested that released PDF affects dorsal clock neurons (Helfrich-Förster et al. 2000). Indeed, ectopic expression of PDF in neurons that project to the dorsal brain region causes severe rhythm defects, suggesting that misregulation of this signaling causes circadian system dysfunction (Helfrich-Förster et al. 2000). Our staining with a PDF peptide indicates that the PDF signaling to the DNs may be direct. Although rhythmic PDF staining is restricted to the s-LNv terminals (Park et al. 2000), this could be because a smaller fraction of PDF is released from the l-LNv terminals. Some of these processes follow the posterior optic track to the opposite side of the brain. Taken together with the LNv peptide staining, it is likely that PDF from the l-LNvs signals contralaterally and positively influences clock cells on the opposite side of the brain. A very recent study of the Drosophila prothoracic gland (PG) clock and eclosion rhythms suggests that the LNvs also control the PG clock via PDF signaling (Myers et al. 2003). This raises the possibility that PDF not only synchronizes brain clock neurons, but also keeps peripheral clocks in pace with the core brain network.

The Pdf01 molecular phenotype implies that the wild-type organization of the system normally supports the individual clock cells as well as the entire circadian program in DD. Although we do not know that all molecular aspects of rhythms damp in DD in Pdf01 flies, we suggest that damped transcriptional rhythms are the intracellular default state in Drosophila and are manifest without the driving and entraining LD cycle or without a functionally integrated clock network. This view is also consistent with recent studies showing that electrical silencing of clock neurons eliminates free-running molecular as well as behavioral rhythms (Nitabach et al. 2002). It will be interesting to learn how PDF signaling connects to the intracellular transcriptional machinery.

We note that communication among clock neurons is likely to be important in other organisms. The ability of PDF to phase-shift the cockroach circadian clock (Petri and Stengl 1997) is more consistent with our proposal than with a simple role in clock output. A recent study of VPAC(2) receptor knock-out mice (Harmar et al. 2002) showed that these mice fail to sustain behavioral rhythms and have molecular rhythms defects within the SCN. This raises the intriguing possibility that SCN neurons as well as Drosophila clock neurons may require network integration to sustain free-running intracellular oscillations.

Materials and Methods


Drosophila genetics.
Full-length cyc cDNA was obtained from BDGP cDNA clone GM02625 and was tagged with hemagglutinin (HA) epitope by PCR cloning. CYC–HA was subsequently cloned into pUAST to generate pUAS–CYC–HA. The transformation plasmid was used to generate transgenetic flies. A third chromosome insertion line (UAS–CYC–HA15) was used subsequently. All wild-type flies and specimens were taken from a Canton-S stock.

The circadian driver lines pdf–GAL4 (Renn et al. 1999), tim–GAL4 (Kaneko and Hall 2000), as well as the cyc01 (Rutila et al. 1998) and Pdf01 (Renn et al. 1999) mutant strains have been previously described. All molecular and behavioral analyses were conducted on flies entrained at 25°C.

GFP expression analysis.
To visualize the axon projections from circadian neurons, a UAS–mCD8GFP line labeling the cell membrane was crossed with various circadian GAL4 drivers. The progeny brains were dissected in PBS and fixed in 3.7% paraformaldehyde in PEM. After rinses in PBS plus 0.3% Triton and PBS, brains were mounted in Vectashield mounting medium (Vector Laboratories, Burlingame, California, United States) and imaged on a Leica laser scanning confocal microscope. Optical sections were taken at 1–2 μm intervals and used to construct a maximum projection image for each brain.

In situ mRNA hybridization on adult brain whole mounts.
In situ hybridization of tim and cry was done as described previously (Zhao et al. 2003). The maximum projection images taken from a Leica laser scanning confocal microscope were used for the quantification. The quantification was done using three brain images per sample with Leica confocal software. The mean pixel intensities of cell groups were normalized by subtracting the average of two general background areas in the brain.

Behavioral analysis.
Flies were entrained for 3–5 d in 12 h light:12 h dark (LD) conditions before release into DD. Locomotor activities of individual flies were monitored using Trikinetics Drosophila Activity Monitors (Waltham, Massachusetts, United States). The analysis was done by using a signal processing toolbox (Levine et al. 2002b). Autocorrelation and spectral analysis were used to assess rhythmicity and to estimate the period. The phase information was extracted using circular statistics (Levine et al. 2002b). In some cases, the phases of individual Pdf01 flies were also examined by inspection.

In vitro peptide binding assay.
Biotinylation of the PDF peptide was with EZ-Link Sulfo–NHS–LC–Biotin reagent (Pierce Biotechnology, Rockford, Illinois, United States), following the manufacturer's instruction. Excess biotinylation reagent was removed by prolonged incubation in Tris–HCl buffer (1 M [pH 7.5]) followed by protein purification through a Polyacrylamide 1800 desalting column (Pierce Biotechnology). A control neuropeptide, allatostatin I (Sigma-Aldrich, St. Louis, Missouri, United States), was biotinylated using the same method. A second control was a synthetic, biotinylated peptide derived from the Drosophila PER protein (a gift from P. Nawathean). In addition, a new N-terminus biotinylated PDF peptide was chemically synthesized de novo (Sigma-Aldrich). Identical results were obtained with the two PDF peptides, and no specific signal was obtained with the two control peptides.

To detect the binding of the neuropeptide in the CNS of Drosophila, brains were dissected in PBS and fixed in 3.7% paraformaldehyde in PEM for 30 min. After they were rinsed in PBS plus 0.3% Triton and blocked using 1% FBS or BSA, biotinylated peptide was incubated with the brains at a final concentration of 0.2 μg/ml. The brains were washed thoroughly with TNT (0.1 M Tris–HCl [pH 7.5], 0.15 M NaCl, 0.05% Tween 20). The bound peptide was subsequently detected through the biotin label using streptavidin–HRP (NEN LifeScience, now Perkin-Elmer, Torrance, California, United States) and fluorescent tyramides (NEN LifeScience). A detailed protocol is provided as Protocol S1. For the competition assay, unlabeled peptide was added at a 200- to 5000-fold concentration increase in the blocking step; subsequent steps were as described above.

Supporting Information
Figure S1 Rescued Molecular Oscillations Persist during DD in the s-LNvs
The “rescued” mutant y w; pdf–GAL4;UAS–CYC,cyc01/cyc01 was released into DD after entrainment and assayed by tim whole-mount in situ hybridization on the fourth day of DD. A Pdf probe was used to label the LNv group. Brains were taken at two opposite timepoints, CT3 (top panels) and CT15 (bottom panels). From left to right are Pdf (green, FITC labeled), tim (red, Cy3 labeled), and an image overlay. The lower arrows point to the s-LNvs and the upper arrows to l-LNvs. Whereas the l-LNvs show barely visible tim RNA oscillations under these conditions, the s-LNvs are obviously cycling. This difference suggests that the l-LNvs might damp more rapidly or be more light-dependent than the s-LNvs in this unusual genotype. (7.1 MB PDF).

Click here for additional data file.

 Protocol S1 Short Protocol for Neuropeptide Biotinylation and Receptor Detection
(23 KB DOC).

Click here for additional data file.

 We thank our colleagues Joan Rutila for making the UAS–CYC–HA transgenetic flies; Jie Zhao for help with the whole-mount in situ hybridization; Patrick Emery and Mike McDonald for inspiration and helpful discussions; Paul Taghert, Orie Shafer, Ravi Allada, and Ralf Stanewsky for critical readings of the manuscript and exchanging unpublished results. We also thank Ed Dougherty and National Institutes of Health (NIH) grant S10 RR16780 for assistance in confocal microscopy and Heather Felton for administrative assistance. The work was supported in part by NIH grants GM33205 and NS44232 to MR and JCH.


Conflicts of Interest. The authors have declared that no conflicts of interest exist.


Author Contributions. YP, DS, JCH, and MR conceived and designed the experiments. YP, DS, and JDL performed the experiments. YP, DS, JDL, and MR analyzed the data. YP, DS, JDL, and MR contributed reagents/materials/analysis tools. YP, DS, and MR wrote the paper.

Academic Editor: Ueli Schibler, University of Geneva.

Abbreviations
clk
clock


cry
cryptochrome


cyc
cycle


CTcircadian time

DDconstant darkness

DNdorsal neuron

HAhemagglutinin

LDlight–dark

l-LNvlarge ventral lateral neuron

LNddorsal lateral neuron

LNvventral lateral neuron

PDFpigment-dispersing factor

per
period


PGprothoracic gland

SCNsuprachiasmatic nucleus

s-LNvsmall ventral lateral neuron

tim
timeless


ZTZeitgeber time.
==== Refs
References
Allada R  White N  So W  Hall J  Rosbash M   A mutant Drosophila  homolog of mammalian Clock disrupts circadian rhythms and transcription of period  and timeless 
 Cell 1998 93 791 804 9630223 
Allada R  Emery P  Takahashi JS  Rosbash M   Stopping time: The genetics of fly and mouse circadian clocks Ann Rev Neurosci 2001 24 1091 1119 11520929 
Allada R  Kadener S  Nandakumar N  Rosbash M   A recessive mutant of Drosophila  Clock reveals a role in circadian rhythm amplitude EMBO J 2003 22 3367 3375 12839998 
Bae K  Lee C  Hardin PE  Edery I   dCLOCK is present in limiting amounts and likely mediates daily interactions between the dCLOCK–CYC transcription factor and the PER–TIM complex J Neurosci 2000 20 1746 1753 10684876 
Balsalobre A  Damiola F  Schibler U   A serum shock induces circadian gene expression in mammalian tissue culture cells Cell 1998 93 929 937 9635423 
Cyran S  Buchsbaum A  Reddy K  Lin M  Glossop N    
vrille , Pdp1 , and dClock  form a second feedback loop in the Drosophila  circadian clock Cell 2003 112 329 341 12581523 
Dowse H  Hall J  Ringo J   Circadian and ultradian rhythms in period mutants of Drosophila melanogaster 
 Behav Genet 1987 17 19 35 3109369 
Dunlap JC   Molecular bases for circadian clocks Cell 1999 96 271 290 9988221 
Emery P  So W  Kaneko M  Hall J  Rosbash M   CRY, a Drosophila  clock and light-regulated cryptochrome, is a major contributor to circadian rhythm resetting and photosensitivity Cell 1998 95 669 679 9845369 
Emery P  Stanewsky R  Helfrich-Förster C  Emery-Le M  Hall JC    
Drosophila  CRY is a deep brain circadian photoreceptor Neuron 2000 26 493 504 10839367 
Giebultowicz J  Stanewsky R  Hall J  Hege D   Transplanted Drosophila  excretory tubules maintain circadian clock cycling out of phase with the host Curr Biol 2000 10 107 111 10662674 
Glossop NRJ  Hardin PE   Central and peripheral circadian oscillator mechanisms in flies and mammals J Cell Sci 2002 115 3369 3377 12154068 
Glossop NRJ  Lyons LC  Hardin PE   Interlocked feedback loops within the Drosophila  circadian oscillator Science 1999 286 766 768 10531060 
Glossop NRJ  Houl JH  Zheng H  Ng FS  Dudek SM    VRILLE feeds back to control circadian transcription of clock in the Drosophila  circadian oscillator Neuron 2003 37 249 261 [Source corrected - 10/23/03] 12546820 
Hall J   Genetics and molecular biology of rhythms in Drosophila  and other insects Adv Genet 2003 48 1 280 12593455 
Hardin P   Analysis of period  mRNA cycling in Drosophila  head and body tissues indicates that body oscillators behave differently from head oscillators Mol Cell Biol 1994 14 7211 7218 7935436 
Hardin PE  Hall JC  Rosbash M   Behavioral and molecular analyses suggest that circadian output is disrupted by disconnected mutants in D. melanogaster 
 EMBO J 1992 11 1 6 1740100 
Harmar A  Marston H  Shen S  Spratt C  West K    The VPAC(2) receptor is essential for circadian function in the mouse suprachiasmatic nuclei Cell 2002 109 497 508 12086606 
Helfrich-Förster C   The period  clock gene is expressed in central nervous system neurons which also produce a neuropeptide that reveals the projections of circadian pacemaker cells within the brain of Drosophila melanogaster 
 Proc Natl Acad Sci U S A 1995 92 612 616 7831339 
Helfrich-Förster C   Robust circadian rhythmicity of Drosophila melanogaster  requires the presence of lateral neurons: A brain-behavioral study of disconnected mutants J Comp Physiol [A] 1997 182 435 453 
Helfrich-Förster C  Tauber M  Park JH  Muhlig-Versen M  Schneuwly S    Ectopic expression of the neuropeptide pigment-dispersing factor alters behavioral rhythms in Drosophila melanogaster 
 J Neurosci 2000 20 3339 3353 10777797 
Kaneko M  Hall JC   Neuroanatomy of cells expressing clock genes in Drosophila : Transgenic manipulation of the period  and timeless  genes to mark the perikarya of circadian pacemaker neurons and their projections J Comp Neurol 2000 422 66 94 10842219 
Krishnan B  Levine J  Lynch M  Dowse H  Funes P    A new role for cryptochrome in a Drosophila  circadian oscillator Nature 2001 411 313 317 11357134 
Levine J  Funes P  Dowse H  Hall J   Advanced analysis of a cryptochrome mutation's effects on the robustness and phase of molecular cycles in isolated peripheral tissues of Drosophila 
 BMC Neurosci 2002a 3 5 11960556 
Levine J  Funes P  Dowse H  Hall J   Signal analysis of behavioral and molecular cycles BMC Neurosci 2002b 3 1 11825337 
Marrus S  Zeng H  Rosbash M   Effect of constant light and circadian entrainment of perS  flies: Evidence for light-mediated delay of the negative feedback loop in Drosophila 
 EMBO J 1996 15 6877 6886 9003764 
Myers EM  Yu J  Sehgal A   Circadian control of eclosion: Interaction between a central and peripheral clock in Drosophila melanogaster 
 Curr Biol 2003 13 526 533 12646138 
Nitabach MN  Blau J  Holmes TC   Electrical silencing of Drosophila  pacemaker neurons stops the free-running circadian clock Cell 2002 109 485 495 12086605 
Panda S  Hogenesch J  Kay S   Circadian rhythms from flies to human Nature 2002 417 329 335 12015613 
Park JH  Helfrich-Förster C  Lee G  Liu L  Rosbash M    Differential regulation of circadian pacemaker output by separate clock genes in Drosophila 
 Proc Natl Acad Sci U S A 2000 97 3608 3613 10725392 
Petri B  Stengl M   Pigment-dispersing hormone shifts the phase of the circadian pacemaker of the cockroach Leucophaea maderae 
 J Neurosci 1997 17 4087 4093 9151725 
Plautz JD  Kaneko M  Hall JC  Kay SA   Independent photoreceptive circadian clocks throughout Drosophila 
 Science 1997 278 1632 1635 9374465 
Rao K  Riehm J   Pigment-dispersing hormones Ann N Y Acad Sci 1993 680 78 88 8512238 
Renn SCP  Park JH  Rosbash M  Hall JC  Taghert PH   A pdf  neuropeptide gene mutation and ablation of PDF neurons each cause severe abnormalities of behavioral circadian rhythms in Drosophila 
 Cell 1999 99 791 802 10619432 
Rutila JE  Suri V  Le M  So WV  Rosbash M    CYCLE is a second bHLH–PAS clock protein essential for circadian rhythmicity and transcription of Drosophila period  and timeless 
 Cell 1998 93 805 814 9630224 
Schibler U  Sassone-Corsi P   A web of circadian pacemakers Cell 2002 111 919 922 12507418 
Sehgal A  Price J  Man B  Young M   Loss of circadian behavioral rhythms and per  RNA oscillations in the Drosophila  mutant timeless 
 Science 1994 263 1603 1606 8128246 
Shafer OT  Rosbash M  Truman JW   Sequential nuclear accumulation of the clock proteins Period and Timeless in the pacemaker neurons of Drosophila melanogaster 
 J Neurosci 2002 22 5946 5954 12122057 
Stanewsky R  Jamison CF  Plautz JD  Kay SA  Hall JC   Multiple circadian-regulated elements contribute to cycling period gene expression in Drosophila 
 EMBO J 1997 16 5006 5018 9305642 
Stanewsky R  Kaneko M  Emery P  Beretta B  Wager-Smith K    The cryb   mutation identifies cryptochrome as a circadian photoreceptor in Drosophila 
 Cell 1998 95 681 692 9845370 
Sujino M  Masumoto K  Yamaguchi S  van der Horst GT  Okamura H    Suprachiasmatic nucleus grafts restore circadian behavioral rhythms of genetically arrhythmic mice Curr Biol 2003 13 664 668 12699623 
Toma DP  White KP  Hirsch J  Greenspan RJ   Identification of genes involved in Drosophila melanogaster  geotaxis, a complex behavioral trait Nat Genet 2002 31 349 353 12042820 
Yang Z  Sehgal A   Role of molecular oscillations in generating behavioral rhythms in Drosophila 
 Neuron 2001 29 453 467 11239435 
Zhao J  Kilman VL  Keegan KP  Peng Y  Emery P    
Drosophila  clock can generate ectopic circadian clocks Cell 2003 113 755 766 12809606

PMID: 12975657
Accession ID: PMC193605
License: CC BY
Last Updated: 2021-01-05 08:21:03
Retracted: no
Citation: PLoS Biol. 2003 Oct 15; 1(1):e19
==== Front
PLoS BiolPLoS BiolpbioplosbiolPLoS Biology1544-91731545-7885Public Library of Science San Francisco, USA 10.1371/journal.pbio.0000019Research ArticleEvolutionGenetics/Genomics/Gene TherapyMicrobiologyEubacteriaFrom Gene Trees to Organismal Phylogeny in Prokaryotes:The Case of the γ-Proteobacteria From Gene Trees to Organismal PhylogenyLerat Emmanuelle 
1
Daubin Vincent 
2
Moran Nancy A nmoran@email.arizona.edu
1
1Department of Ecology and Evolutionary Biology, University of ArizonaTucson, ArizonaUnited States of America2Department of Biochemistry and Molecular Biophysics, University of ArizonaTucson, ArizonaUnited States of America10 2003 15 9 2003 15 9 2003 1 1 e196 6 2003 30 7 2003 Copyright: © 2003 Lerat et al.2003This is an open-access article distributed under the terms of the Creative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are properly credited.
New Genomic Approach Predicts True Evolutionary History of Bacterial Genomes 
The rapid increase in published genomic sequences for bacteria presents the first opportunity to reconstruct evolutionary events on the scale of entire genomes. However, extensive lateral gene transfer (LGT) may thwart this goal by preventing the establishment of organismal relationships based on individual gene phylogenies. The group for which cases of LGT are most frequently documented and for which the greatest density of complete genome sequences is available is the γ-Proteobacteria, an ecologically diverse and ancient group including free-living species as well as pathogens and intracellular symbionts of plants and animals. We propose an approach to multigene phylogeny using complete genomes and apply it to the case of the γ-Proteobacteria. We first applied stringent criteria to identify a set of likely gene orthologs and then tested the compatibilities of the resulting protein alignments with several phylogenetic hypotheses. Our results demonstrate phylogenetic concordance among virtually all (203 of 205) of the selected gene families, with each of the exceptions consistent with a single LGT event. The concatenated sequences of the concordant families yield a fully resolved phylogeny. This topology also received strong support in analyses aimed at excluding effects of heterogeneity in nucleotide base composition across lineages. Our analysis indicates that single-copy orthologous genes are resistant to horizontal transfer, even in ancient bacterial groups subject to high rates of LGT. This gene set can be identified and used to yield robust hypotheses for organismal phylogenies, thus establishing a foundation for reconstructing the evolutionary transitions, such as gene transfer, that underlie diversity in genome content and organization.

The study demonstrates that single-copy orthologous genes are resistant to horizontal transfer and can be used to generate robust hypotheses for organismal phylogenies
==== Body
Introduction
The availability of complete sequences of genomes for clusters of related organisms presents the first opportunity to reconstruct events of genomic evolution. By comparing related genomes and inferring ancestral ones, we can identify events, such as specific chromosomal rearrangements, gene acquisitions, duplications, and deletions, that have produced the observed diversity in genome content and organization. The Bacteria offer the most immediate opportunities for such reconstruction, because many clusters of related genomes are now available and because the genomes are small and contain relatively little repetitive sequence, reducing computational complexity. Among bacterial groups, the γ-Proteobacteria presents the most intensively studied and sequenced cluster of genomes with varying degrees of relatedness.

Intertwined with the problem of reconstructing genomic change is the problem of inferring phylogeny. Evading this issue is particularly difficult in the Bacteria. First, using complete genomes to obtain a robust phylogeny for all bacteria has presented problems due to the age of the group and the resulting loss of phylogenetic signal. Furthermore, lateral gene transfer (LGT) occurs in bacteria and has been claimed to be rampant for all classes of genes, potentially resulting in a diversity of phylogenetic histories across genes and complicating, or completely defeating, attempts to reconstruct bacterial evolution at both deep and more recent evolutionary depths (Doolittle 1999; Nesbø et al. 2001; Gogarten et al. 2002; Wolf et al. 2002; Zhaxybayeva and Gogarten 2002). Although the existence of substantial levels of LGT in bacterial genomes is not disputed, the existence of a core of genes resistant to LGT has been proposed (Jain et al. 1999) and has received some support from recent studies using relatively intensive taxon sampling (Brochier et al. 2002; Daubin et al. 2002).

For purposes of reconstructing genomic change, what we seek is the organismal phylogeny—that is, the topology that traces the history of the replicating cell lineages that transmit genes and genomes to successive generations. The organismal phylogeny provides the backdrop against which events of genomic change, including LGT, have occurred. High incidence of LGT may cause the organismal phylogeny to be elusive, because we do not know which genes represent the true history of the cell lineages.

The gene most used for reconstructing organismal phylogeny is the small subunit ribosomal RNA (SSU rRNA), which has been argued to rarely undergo transfer among genomes (Woese 1987; Jain et al. 1999). But even this gene may undergo occasional LGT or recombination (Ueda et al. 1999; Yap et al. 1999). Furthermore, by itself, it provides insufficient information to resolve phylogenies, particularly for cases of heterogeneous rates and patterns of substitution. Thus, building conclusions about organismal phylogeny on the basis of SSU rRNA alone is unsatisfactory. The availability of complete genome sequences presents us with the potential to exploit the much greater set of genes that are expected to share the same history of transmission along the branches of the organismal phylogeny. A robust phylogeny based on more sequences could then be used to reconstruct genome-scale events, including LGT and rearrangements. But, while complete genome sequences have enormous potential for addressing phylogenetic issues, their utility for reconstructing bacterial phylogeny is initially quite limited due to the requirement of thorough taxon sampling within a clade for accurate reconstruction of phylogenies (Zwickl and Hillis 2002; Hillis et al. 2003). Only now, with the continuing increase in numbers of fully sequenced bacterial species, is it becoming possible to obtain sufficiently dense taxon sampling to exploit the large amount of genomic sequence data for the purpose of phylogeny reconstruction.

We have chosen one group of Bacteria, the γ-Proteobacteria, to address the problem of whether complete genome sequences can be used for robust reconstruction of the organismal phylogeny, despite high levels of LGT. The γ-Proteobacteria, distinguished on the basis of sequence signatures and structural differences in the SSU rRNA (Woese 1987), is an ideal choice for this purpose. This group represents a model of bacterial diversification and includes free-living and commensal species, intracellular symbionts, and plant and animal pathogens. The sequence divergence of certain of its members (Clark et al. 1999) suggests an age of at least 500 million years. At the same time, members are sufficiently closely related to enable us to reduce the problem of lack of phylogenetic signal and to identify a large set of unambiguous orthologs. Currently, the γ-Proteobacteria contains the highest density of fully sequenced genomes, including those of species (Escherichia coli and Salmonella sp.) for which knowledge of gene function is more complete than for any other cellular organisms. The potential obstacles to phylogenetic inference that are found across the Bacteria are certainly present in the γ-Proteobacteria. In particular, LGT is known to be extensive in this group, based on studies of genome composition (Lawrence and Ochman 1997; Parkhill et al. 2000, 2001; Stover et al. 2000). Symbiotic lineages present particular issues for phylogeny reconstruction owing to huge losses of genes (Shigenobu et al. 2000; Akman et al. 2002), accelerated sequence evolution, and shifts in base composition (Moran 1996). These features create phylogenetic artifacts and make the use of additional data from genome sequences particularly desirable.

Here we aim to use complete genome sequences to reconstruct the organismal phylogeny for the γ-Proteobacteria by first selecting a set of probable ortholog families and then determining whether most agree on a common topology. A major implication of our results is that the replacement of single-copy orthologous genes is extremely rare, even within phyla. Instead, LGT most often involves uptake of genes assuming functions that are not represented in the recipient and arriving from distantly related bacteria or from phage (Daubin et al. 2003a; Pedulla et al. 2003). A consequence is that most single-copy orthologous genes show broad phylogenetic agreement that reflects the organismal relationships and that provides a foundation for reconstructing events of genome evolution.

Results
Gene Families and Identification of Orthologous Genes
The proteins of 13 complete γ-proteobacterial genomes were classified into an initial set of 14,158 homolog families, using the procedures described in Materials and Methods. Figure 1A shows the distribution of the number of genes per family. A majority (7,655) of the families contain only one gene. As the criteria we applied for grouping genes into families are stringent, this number is expected to exceed the number of real orphan genes; indeed, annotations for many of these genes do claim homology with other genes in the included genomes. As a result, values for most of the genomes (Figure 1B) are higher than the number of genes annotated as orphans; for example, the number of this type of gene identified for Buchnera was 24, but the annotation indicates only four genes unique to this species (Shigenobu et al. 2000). Moreover, our comparison was made only within this group of 13 bacteria, and some single-gene families may have homologs in other, more distant bacterial species. Pseudomonas aeruginosa yielded the highest number of unique genes, which represent nearly 41% of proteins of this genome. This is congruent with the result obtained during the original annotation of this genome: the authors were unable to identify relatives for 32% of the ORFs (Stover et al. 2000).

Figure 1 Number of Genes and Species within the Gene Families
(A) Distribution of the number of genes contained in the homolog families.

(B) Number of orphan genes in each species in parentheses. Abbreviations: Ba, Buchnera aphidicola; Ec, Escherichia coli; Hi, Haemophilus influenzae; Pa, Pseudomonas aeruginosa; Pm, Pasteurella multocida; St, Salmonella typhimurium; Vc, Vibrio cholerae; Wb, Wigglesworthia brevipalpis; Xa, Xanthomonas axonopodis; Xc, Xanthomonas campestris; Xf, Xylella fastidiosa; Yp CO92, Yersinia pestis CO_92; Yp KIM, Yersinia pestis KIM.

(C) Distribution of the number of species contained in the homolog families.

At the other extreme, some families group large numbers of genes. The largest family contains 544 genes and corresponds to the ABC transporter family, known to be the largest protein family (Tatusov et al. 1996; Tomii and Kanehisa 1998). The second-largest family, with 404 genes, corresponds to the histidine kinase response regulators (Wolanin et al. 2002).


Figure 1C shows the distribution of number of species per gene family. Note that a large majority of families group only one or two species (8,035 and 2,693 families, respectively). In the families comprising only one species, Pseudomonas and Vibrio are heavily represented, with 2,397 and 1,474 families, respectively. The families containing two species often group two closely related genomes, such as the two Xanthomonas, the two Yersinia, Escherichia and Salmonella, and Haemophilus and Pasteurella.

A total of 275 families are represented in all 13 species. Among these, 205 contain exactly one gene per species. We consider these 205 genes to represent likely orthologs and, consequently, to be good candidates for use in inferring the organismal phylogeny and the extent of LGT.

The Extent of Conflict among Gene Families
We constructed trees based on several combinations of data and methods (see Materials and Methods), with the aim of generating a set of candidate topologies for the organismal phylogeny. These seven analyses produced a total of six topologies (numbered 1–6 in Figure 2). (The identical topology was obtained for the consensus tree and the tree based on the protein concatenation using the neighbor-joining [NJ] method and the γ-based method for correcting the rate heterogeneity among sites.) The trees differ, in particular, with regard to the positions of Wigglesworthia, Buchnera, and Vibrio. All topologies, except number 4 (that one resulting from the Galtier and Gouy distance method with the SSU rRNA), tend to place Wigglesworthia and Buchnera as sister taxa (Figure 2). The sister relationship of Wigglesworthia and Buchnera was of particular interest because it would suggest a shared origin of symbiosis in an ancestor of these two species. Thus, we tested seven additional topologies (numbered 7–13 on Figure 2) that did not place these two species as sister taxa, but that otherwise resembled topologies 1–6.

Figure 2 The 13 Candidate Topologies
Topologies 1–4 correspond to tree reconstructions based on SSU rRNA. Topologies 5 and 6 correspond to the trees based on the concatenation of the proteins. Topologies 7–13 correspond to additional topologies constructed to test the sister relationship of the two symbiont species. Species abbreviations as in Figure 1. Abbreviations: ML, maximum likelihood; NJ, neighbor joining; K, Kimura distance; G&G, Galtier and Gouy distance; γ, gamma-based method for correcting the rate heterogeneity among sites. The position of the root corresponds to the one obtained repeatedly using SSU rRNA.

For each alignment, we tested the likelihood of the 13 topologies against the maximum-likelihood (ML) topology, using the Shimodaira–Hasegawa (SH) test, as recommended by Goldman et al. (2000). The question asked here was whether the tested topologies could be considered equally good explanations of the data. Figure 3 shows the result of this test. One topology (number 5) is in agreement with 203 of 205 alignments (Figure 3). Three other slightly different topologies can be considered nearly as good on the basis of agreement with a large majority of alignments (for topologies 2, 3, and 6 agreement was with 197, 196, and 186 alignments, respectively; Figure 3).

Figure 3 Result of the SH Test
The graph shows the number of alignments accepting or rejecting each topology. The “Other Topologies” are those built to test the sister relationship of Wigglesworthia and Buchnera. The “Proteins” topologies are those obtained using both the protein concatenation and the consensus of trees from all 205 alignments. The “SSU rRNA” topologies were obtained using the SSU rRNA sequences with different methods.

Cases of Lateral Transfer
Of the 205 alignments, two were found to strongly reject the most accepted tree (topology 5) as well as all other topologies tested. We have investigated these two genes to determine whether the incongruence is likely to result from LGT. The proteins correspond to biotin synthase (BioB) and to the virulence factor MviN. The trees obtained using ML for each alignment are shown in Figure 4A. In both cases, the position of Pseudomonas conflicts with all widely supported topologies; it is placed as sister-group to Vibrio (BioB) or as sister-group to the enterics Escherichia, Salmonella, and Yersinia (MviN). Although initial examination of the topologies obtained from these genes suggests more than a single LGT (comparing trees of Figure 4A to topology 5 of Figure 2), the hypothesis of a single transfer in an ancestor of Pseudomonas could not be rejected for either gene based on the results of the SH test after removal of Pseudomonas from the alignments and from topology 5 and other widely supported phylogenies. The implication is that a single transfer event in an ancestor of Pseudomonas is sufficient to explain the conflict of bioB and mviN with trees derived from other genes. In addition, we searched GenBank for homologous genes in other species of Pseudomonas and built trees using NJ and the Poisson correction (Figure 4B). In each case, Pseudomonas species are grouped and display the same position as in the trees, based only on the 13 sequenced genomes (Figure 4A). Moreover, the bootstrap support was high for the grouping of Pseudomonas with Vibrio in the BioB tree and for the grouping of Pseudomonas with the enteric bacteria in the MviN tree. Thus, the phylogeny of each of these two genes can be explained as the result of a single LGT event, from different donors within the γ-Proteobacteria to a shared ancestor of these Pseudomonas species.

Figure 4 Phylogenies for the Laterally Transferred Genes
(A) ML trees obtained for BioB (left) and MviN (right). (B) NJ trees obtained for BioB (left) and MviN (right). Abbreviations: Pf, Pseudomonas fluorescens; Pp, Pseudomonas putida; Ps, Pseudomonas syringae. Other species abbreviations as in Figure 1.

In Escherichia, Vibrio, Salmonella, Yersinia, and Pseudomonas, bioB is flanked by bioF, also involved in biotin biosynthesis. To determine whether bioF could have been transferred with the bioB gene, we built a tree based on the protein translation of bioF using all species except Buchnera, Haemophilus, and Pasteurella, which lack this gene. The tree obtained did not show any unexpected position of Pseudomonas, indicating that only bioB has been horizontally transmitted. A possible explanation, consistent with the flanking position of bioB and bioF in the Pseudomonas genome, is that the original bioB gene was replaced through homologous recombination in a common ancestor of the included Pseudomonas species. Similar comparisons for mviN did not illuminate its history in Pseudomonas, as the flanking genes differed from those in other species. The observations for mviN are consistent with a transfer event from an enteric species to a new genomic position in a Pseudomonas ancestor.

Robustness of the Inferred Organismal Phylogeny
The general lack of conflict observed among the 203 remaining families was not due to the absence of phylogenetic signal in the gene alignments because most genes did conflict with several other topologies (see Figure 3). We interpreted this congruence as a reflection of shared history and a lack of LGT. Therefore, we chose these genes as the basis for inferring the true organismal phylogeny for these 13 species. The resulting tree was the same as that for the concatenation of all of the 205 genes and for the consensus of the trees obtained from all protein families (topology 5 in Figure 2 and tree presented in Figure 5). It differed only slightly from other tested topologies (see Figure 2) that also are not rejected by many individual alignments (see Figure 3). Finally, an SH test performed using the complete concatenated alignment shows that this topology is significantly more likely than all alternative hypotheses.

Figure 5 Tree Based on the Concatenation of the 205 Proteins (NJ)
The topology shown agrees with almost all individual gene alignments (topology 5 of Figure 2). The same tree is obtained after removing the two genes showing evidence for LGT. The position of the root corresponds to the one obtained repeatedly using SSU rRNA.

All topologies separating Wigglesworthia and Buchnera were rejected by the majority of the alignments. In the best-supported topology (see Figure 5), Wigglesworthia and Buchnera are grouped and comprise the sister-group to the enteric bacteria Yersinia, Salmonella, and Escherichia. Previously published phylogenies, based on SSU rRNA, gave conflicting results for the positions of these symbionts, sometimes placing Buchnera as sister-group to Escherichia and Salmonella (van Ham et al. 1997; Spaulding and von Dohlen 1998; Moya et al. 2002). Because the genomes of these endosymbionts present a strong bias toward A+T relative to other genomes in the set, their grouping could reflect convergence at some nucleotide sites. This convergence could affect both the SSU rRNA, which is enriched in A+T (Moran 1996), and also the protein sequences, which are enriched in amino acids with A+T-rich codon families (Clark et al. 1999). To test this hypothesis, we removed from the alignment of the protein concatenation all sites at which Buchnera and Wigglesworthia contain amino acids encoded by A+T-rich codons (phenylalanine, tyrosine, methione, isoleucine, asparagine, and lysine) (Singer and Hickey 2000). Using the resulting alignment (about 30,000 residues), we have reconstructed two trees, one with the NJ method and the polyacid-modified (PAM) matrix; the other with the NJ method and the γ-based method for correcting the rate heterogeneity among sites and bootstrap. The trees obtained (data not shown) were identical and gave strong support to the grouping of Buchnera and Wigglesworthia and to their position as the sister-group of enteric bacteria (Escherichia, Salmonella, and Yersinia). Thus, this grouping is probably not an artifact of the biased composition of the endosymbiont genomes.

Discussion
The most striking result is the almost complete lack of conflict among the set of genes selected as likely orthologs. Only two of 205 ortholog families showed such disagreement, both involving the P. aeruginosa genome. Because the γ-Proteobacteria has been the bacterial group most often cited as showing high rates of LGT, this finding is unexpected. However, we note that the evidence for LGT from sequence features and comparisons of genome content (Lawrence and Ochman 1997; Ochman and Jones 2000; Parkhill et al. 2001; Perna et al. 2001; Daubin et al. 2003a) primarily implicate genes that are absent from related bacteria; such genes would not have been retained in our set of putative orthologs. Furthermore, such genes are not candidates for phylogeny reconstruction since they are missing from most taxa. We also eliminated the large set of homolog families present as more than one sequence within even one of the genomes. If families containing paralogs show relatively high susceptibility to LGT, the proportion of genes undergoing LGT would be underestimated by considering only the set with one sequence per genome. Our aim was to locate a set of genes giving strong and consistent signal regarding the organismal phylogeny, and our results do not imply a lack of LGT in genes other than the widespread, single-copy orthologs that we selected. By streamlining the dataset for our primary goal, we have excluded genes that undergo more frequent transfer.

Phylogenetic evidence for LGT mostly involves transfer between distantly related organisms (Nelson et al. 1999; Brown et al. 2001; Brown 2003; Xie et al. 2003), and most clear-cut cases involve genes that are sporadically distributed (e.g., Parkhill et al. 2000; Singer and Hickey 2000) and thus excluded from our selection of families. The selected set includes genes that are distributed across a wide set of bacteria and includes about 100 universally distributed genes, such as those encoding ribosomal proteins, DNA polymerase subunits, and transfer RNA synthetases (Table S1). Thus, if LGT is affecting most categories of genes, it should be detectable in our set, resulting in discordance of phylogenies whether it occurs between related genomes (within the γ-Proteobacteria) or between very dissimilar genomes. Such discordance was extremely rare, affecting only two (1%) of our families.

Several previous studies have provided evidence that a core of genes may resist LGT and give a consistent phylogenetic signal (Jain et al. 1999; Brochier et al. 2002; Daubin et al. 2002). However, the same studies have noted high incidence of genes showing incongruence, and, because they involved deeper trees and incorporated a much less dense sampling of genes or of taxa, this incongruence has not been firmly identified as due to LGT or to phylogenetic artifacts. Furthermore, recent analyses based on other sets of taxa have led to the proposal that all sets of genes, including orthologous genes, are subject to high rates of LGT (Nesbø et al. 2001; Gogarten et al. 2002; Zhaxybayeva and Gogarten 2002), thereby casting doubt on the idea that we can identify a core set of orthologs that reflect the organismal phylogeny. Our analysis indicates that LGT is unusual for single-copy orthologous genes; that is, a gene copy from one species usually does not replace its ortholog in another species. The apparent discrepancy is not due to a relative lack of LGT in this particular group of bacteria, which is known to acquire foreign genes frequently (Lawrence and Ochman 1997; Parkhill et al. 2000; Perna et al. 2001). More likely explanations are that (1) our criterion for orthology was more stringent in ruling out undetected paralogy; (2) the use of quartet phylogenies (Zhaxybayeva and Gogarten 2002) can be misleading owing to artifacts linked to taxon sampling (Zwickl and Hillis 2002); and (3) our focus on a relatively closely related group of bacteria minimizes the problem of loss of phylogenetic signal and reconstruction artifacts in deep divergences. This result thus provides further evidence that, though bacterial genomes constantly acquire and lose significant amounts of DNA, the incidence of LGT for widespread orthologous genes is relatively low (Daubin et al. 2003b). Although we have likely excluded many actual orthologs, the set of retained genes provides a dataset that is sufficiently informative to give a highly resolved and well-supported phylogeny for these taxa.

This study thus defines a minimal core of genes that show both wide representation and congruent phylogenetic signal in γ-Proteobacteria. We note that this core includes numerous genes in both “informational” and “operational” functional categories (Table S1); thus, our results do not fit closely with the “complexity hypothesis,” that only informational genes avoid LGT (Jain et al. 1999), although they do not exclude such a trend. Our set of 203 genes should not be considered as representative of all genes resisting LGT, since we did not explore the other gene families. The main functional feature distinguishing the set is likely to be essentiality, owing to the requirement of presence in all 13 genomes, including the reduced symbiont genomes. For the goal of selecting genes that reflect organismal phylogeny through vertical descent, our criteria (single copy and ubiquitous) appear to be more reliable than criteria based on functional information (informational genes, translational genes, etc.). Indeed, cases of LGT are known for informational genes (e.g., Brochier et al. 2000).

One possible explanation for the lack of observed events of orthologous replacement might be that these are sufficiently rare that significant frequencies are encountered only when considering deeper phylogenetic levels. However, the group studied here, though recent enough to allow accurate phylogenetic reconstruction, is old. Indeed, the divergence of different Buchnera species has been dated to approximately 200 million years based on the host fossil record (Clark et al. 1999), and the clade we have studied must be much more ancient. A conservative molecular clock estimate, based on rRNA and dating the divergence of Escherichia and Buchnera at 200 million years, places the origin of the group at more than 500 million years (calculations not shown). Thus, our finding that very few orthologs have been exchanged within the group and that none show evidence of having been imported from other bacterial lineages is relevant for the understanding of long-term bacterial evolution.

It has been proposed that LGT may be more frequent within clusters of related bacteria and even that phylogenetic groupings, such as the γ-Proteobacteria, may reflect boundaries to LGT rather than recent shared ancestry of lineages (Gogarten et al. 2002). Such a model, which is consistent with apparent concordance among ortholog families in studies with poor taxon sampling but predicts rampant discordance within a well-sampled bacterial cluster, is strongly rejected by our results. Our findings favor the view that the cohesion of major phylogenetic groups within the Bacteria is due to vertical transmission and common ancestry rather than to preferential lateral transfer of genes. However, the results presented here do not eliminate the possibility of nonrandom patterns of LGT for gene families that are more sporadically distributed.

A robust phylogenetic framework for the organismal lineages provides the foundation for reconstructing the events of genome evolution. An example of the kind of biological inference that can be built upon a well-supported phylogeny is provided by the two endosymbionts included in our set. Wigglesworthia and Buchnera have sometimes been considered as closely related and sometimes not, based on relatively weak phylogenetic evidence provided by the SSU rRNA alone. Our confirmation of their close relationship raises the question of whether their common ancestor was an endosymbiont with a reduced genome or a free-living bacterium (perhaps one with a host-associated lifestyle that promoted formation of intimate symbiosis). Because Buchnera and Wigglesworthia do not share any genes absent from the other species, no particular genes can be implicated as conferring a predisposition to symbiosis, a result that eliminates some hypotheses about how symbiosis originates. Furthermore, although emphasis has previously been placed on the close relationship of Buchnera with E. coli, our results shows that the phylogenetic relationship is equally high with other enterics, such as Yersinia pestis, which indeed shares as many ortholog families with Buchnera as does E. coli. This knowledge of relationships to other genomes allows more accurate reconstruction of ancestral genome content and of the chromosomal deletions and rearrangements occurring during the evolution of reduced symbiotic genomes (Moran and Mira 2001).

One biological interpretation of our findings is that the immediate retention of an acquired gene within a lineage depends upon strong positive selection for its function (Ochman et al. 2000) and that such selection is unlikely if a homologous gene is already present in the recipient genome. An implication, from the perspective of phylogeny reconstruction, is that single-copy homologs with widespread distribution are a source of reliable information for inferring organismal phylogeny. The existence of many other gene families with multiple members per genome or with erratic distributions across the set of genomes (see Figure 1) is consistent with a major role of LGT, gene loss, and gene duplication in the evolution of this bacterial clade. Combined with chromosomal rearrangements, these events are the major sources of genomic, and ultimately ecological, diversification of bacterial groups. By demonstrating the potential to establish robust organismal phylogenies using genome sequence data, our results provide a foundation for examining the rates and frequencies of LGT and other large-scale events in evolving genomes.

Materials and Methods

Data.
The genomes chosen for this study correspond to 13 γ-Proteobacterial taxa that show different degrees of relatedness based on divergence of SSU rRNA and that include two symbionts having undergone large-scale genomic reduction (Shigenobu et al. 2000; Akman et al. 2002). The protein sequences of the 13 complete genomes were retrieved from the GenBank database (Benson et al. 2002). The species used were Escherichia coli K12 (accession number NC_000913; Blattner et al. 1997), Buchnera aphidicola APS (NC_002528; Shigenobu et al. 2000), Haemophilus influenzae Rd (NC_000907; Fleischmann et al. 1995), Pasteurella multocida Pm70 (NC_002663; May et al. 2001), Salmonella typhimurium LT2 (NC_003197; McClelland et al. 2001), Yersinia pestis CO_92 (NC_003143; Parkhill et al. 2000), Yersinia pestis KIM5 P12 (NC_004088; Deng et al. 2002), Vibrio cholerae (NC_002505 for chromosome 1 and NC_002506 for chromosome 2; Heidelberg et al. 2000), Xanthomonas axonopodis pv. citri 306 (NC_003919; da Silva et al. 2002), Xanthomonas campestris (NC_003902; da Silva et al. 2002), Xylella fastidiosa 9a5c (NC_002488; Simpson et al. 2000), Pseudomonas aeruginosa PA01 (NC_002516; Stover et al. 2000), and Wigglesworthia glossinidia brevipalpis (NC_004344; Akman et al. 2002).

To identify genes likely to have been transmitted vertically through the history of the γ-Proteobacteria, we first eliminated proteins annotated as elements of insertion sequences or as bacteriophage sequences, since they are likely to be subject to lateral transfer. Such sequences were present in most genomes but lacking in a few (B. aphidicola, W. brevipalpis, and P. multocida). Table 1 shows the number of proteins that remain in each genome after such elimination.

Table 1 Number of Protein-Coding Genes per Genome after Elimination of the Insertion and Bacteriophage Sequences

a Chromosome 1


b Chromosome 2

Construction of the gene families.
We applied a stringent criterion for eliminating nonhomologous sequences and paralogous sequences, since both are likely to lead to false conclusions regarding the organismal phylogeny and frequency of LGT. In particular, the criterion of “best reciprocal hits” between sequences for a genome pair can lead to false conclusions of orthology because the resulting gene pairs are not always closest relatives phylogenetically (Koski and Golding 2001). Instead, we used a cutoff for the degree of similarity as reflected in the BLASTP bit scores (Altschul et al. 1997). The bit score is dependent upon the scoring system (substitution matrix and gap costs) employed and takes into account both the degree of similarity and the length of the alignment between the query and the match sequences. We used it to detect homologous genes, described as follows. A bank of all annotated protein sequences of all included species was created. A BLASTP (Altschul et al. 1997) search was performed for all the proteins in each genome against the protein bank. This implies that all proteins were searched against both their resident genome and those from the 12 other species. The match of a given protein against itself gives a maximal bit score. To determine a threshold to group genes into a family, we examined the distribution of the ratio of the bit score to the maximal (self) bit score based on the proteins of E. coli compared against proteins of the 12 genomes (Figure 6). In each case, the distribution showed a clear bimodal pattern with a first peak of low similarity values, which is constant among comparisons and therefore probably represents random matches, and a second peak of higher similarity values, representing true homologous genes. For comparisons of E. coli proteins with those of the most distant species in our set, such as Vibrio, Xanthomonas, Xylella, and Pseudomonas, the separation of the two portions of the distribution occurs at about 30% of the maximal bit score. Thus, in order to apply a stringent criterion for homology, we inferred as homologous genes those presenting a bit score value higher or equal to 30% of the maximal bit score. A protein was included in a family if this criterion was satisfied for at least one member. Our cutoff was chosen to minimize inclusion of nonhomologous sequences within a family; consequently, it may exclude some homologs, especially fast-evolving ones.

Figure 6 Similarity Levels for Pairwise Comparisons of Genes from Two Representative Genome Pairs
Frequency distribution of the ratio (bit score/maximal bit score) in a BLASTP query of the proteins from E. coli on the proteins from the genomes of Salmonella enterica (solid line) and Vibrio cholerae (dashed line). The ratio of 0.3 allows identification of most homologs but excludes probable nonspecific matches (NS).

After establishing homolog families, we selected the set that contained a single sequence in each represented genome and regarded these as likely orthologs that could give information about the organismal phylogeny and the frequency of LGT affecting orthologs in this bacterial group.

Phylogenies.
The alignments for each identified gene family were created using the CLUSTALW 1.8 program (Thompson et al. 1994). We corrected the concatenated proteins alignment by removing ambiguous parts using the SEAVIEW sequence editor (Galtier et al. 1996). The TREE-PUZZLE 5.1 program (Schmidt et al. 2002) was used in order to determine the α parameter from the datasets for the γ-based method for correcting the rate heterogeneity among sites.

We wished to generate a set of reasonable candidate topologies that could be tested against the alignments for individual genes. These topologies were generated based on the consensus of the 205 trees from individual protein families (one method, yielding topology 5 of Figure 2), on the concatenation of all the proteins (over 75,000 amino acids) (two methods, yielding topologies 5 and 6), and on the SSU rRNA (four methods, yielding topologies 1–4). In the case of the reconstruction of the trees based on the SSU rRNA, we used the DNAML module of the PHYLIP package version 3.6 (Felsenstein 2002), which performs ML reconstruction using the γ-based method for correcting the rate heterogeneity among sites; the PHYLO_WIN program (Galtier et al. 1996) using the NJ method with bootstrap and using two different distances, Kimura 2P distance and Galtier and Gouy distance, designed to reduce bias due to base composition (Galtier et al. 1996); and the MEGA program (Kumar et al. 1993) using the NJ method with bootstrap and with the γ-based method for correcting the rate heterogeneity among sites.

We used the PROML module of the PHYLIP package version 3.6 (Felsenstein 2002) to conduct a ML reconstruction using the Jones, Taylor, and Thornton (JTT) model of substitution (Jones et al. 1992) and the γ-based method for correcting the rate heterogeneity among sites, on each of the 205 families of single-copy, orthologous proteins. The consensus of the trees of the 205 protein alignments was obtained using the CONSENSE module of the PHYLIP package version 3.6 (Felsenstein 2002). As there are no missing data, we also concatenated all the proteins and used the PHYLO_WIN program (Galtier et al. 1996), using the NJ method and the PAM distance matrix, and the MEGA program (Kumar et al. 1993), using the NJ method with bootstrap and with the γ-based method for correcting the rate heterogeneity among sites, on the protein concatenation.

For each of the 205 alignments, a comparison of the likelihood of the best topology with the likelihood of the candidate topologies shown in Figure 2 were performed with the SH test (Shimodaira and Hasegawa 1999) implemented in TREE-PUZZLE 5.1 (Schmidt et al. 2002). This test determines whether these potential organismal phylogenies are significantly rejected by the alignment and thus whether an event of LGT must be invoked.

Finally, we used the SH test to determine whether more than one LGT event was required to explain the lack of congruence between the favored topology and two gene alignments that rejected that topology. For each case, we observed which taxon showed the most evident discordance in the topology derived from the exceptional gene alignment. We then removed the corresponding sequence from the alignment and the corresponding taxon from the widely favored topologies. Using an SH test, we determined whether the alignment continued to show significant conflict with the favored topologies.

Supporting Information
Table S1 Names and Functional Categories of the 205 Genes Used to Reconstruct the Phylogenetical Relationship of γ-Proteobacteria
(123 KB DOC).

Click here for additional data file.

 Accession Numbers
The GenBank accession numbers discussed in this paper are NC_000907, NC_000913, NC_002488, NC_002505, NC_002506, NC_002516, NC_002528, NC_002663, NC_003143, NC_003197, NC_003902, NC_003919, NC_004088, and NC_004344.

We thank Howard Ochman for comments. Support came from National Science Foundation Biocomplexity grant number 9978518.


Conflicts of Interest. The authors have declared that no conflicts of interest exist.


Author Contributions. EL, VD, and NAM conceived and designed the experiments. EL analyzed the data. EL, VD, and NAM wrote the paper.

Academic Editor: David Penny, Massey University.

Abbreviations
BioBbiotin synthase

LGTlateral gene transfer

MLmaximum likelihood

NJneighbor joining

PAMpolyacid modified

SH testShimodaira–Hasegawa test

SSU rRNAsmall subunit ribosomal RNA.
==== Refs
References
Akman L  Yamashita A  Watanabe H  Oshima K  Shiba T    Genome sequence of the endocellular obligate symbiont of tsetse flies, Wigglesworthia glossinidia 
 Nat Genet 2002 32 402 407 12219091 
Altschul SF  Madden TL  Schäffer AA  Zhang J  Zhang Z    Gapped BLAST and PSI-BLAST: A new generation of protein database search programs Nucleic Acids Res 1997 25 3389 3402 9254694 
Benson DA  Karsch-Mizrachi I  Lipman DJ  Ostell J  Rapp BA    GenBank Nucleic Acids Res 2002 30 17 20 11752243 
Blattner FR  Plunkett G  Bloch CA  Perna NT  Burland V    The complete genome sequence of Escherichia coli  K-12 Science 1997 277 1453 1474 9278503 
Brochier C  Philippe H  Moreira D   The evolutionary history of ribosomal protein RpS14: Horizontal gene transfer at the heart of the ribosome Trends Genet 2000 16 529 533 11102698 
Brochier C  Bapteste E  Moreira D  Philippe H   Eubacterial phylogeny based on translational apparatus proteins Trends Genet 2002 18 1 5 11750686 
Brown JR   Ancient horizontal gene transfer Nat Rev Genet 2003 4 121 132 12560809 
Brown JR  Douady CJ  Italia MJ  Marshall WE  Stanhope MJ   Universal trees based on large combined protein sequence data sets Nat Genet 2001 28 281 285 11431701 
Clark MA  Moran NA  Baumann P   Sequence evolution in bacterial endosymbionts having extreme base composition Mol Biol Evol 1999 16 1586 1598 10555290 
da Silva ACR  Ferro JA  Reinach FC  Farah CS  Furlan LR    Comparison of the genomes of two Xanthomonas  pathogens with differing host specificities Nature 2002 417 459 463 12024217 
Daubin V  Gouy M  Perrière G   A phylogenomic approach to bacterial phylogeny: Evidence of a core of genes sharing a common history Genome Res 2002 12 1080 1090 12097345 
Daubin V  Lerat E  Perrière G   The source of lateral gene transfer in bacteria Genome Biol 2003a In press 
Daubin V  Moran N  Ochman H   Phylogenetics and the cohesion of bacterial genomes Science 2003b 301 829 832 12907801 
Deng W  Burland V  Plunkett G  Boutin A  Mayhew GF    Genome sequence of Yersinia pestis  KIM J Bacteriol 2002 184 4601 4611 12142430 
Doolittle WF   Phylogenetic classification and the universal tree Science 1999 284 2124 2129 10381871 
Felsenstein J   PHYLIP (Phylogeny Inference Package), version 3.6 2002 Department of Genetics, University of Washington, Seattle, Washington. Available from http://evolution.genetics.washington.edu/  
Fleischmann RD  Adams MD  White O  Clayton RA  Kirkness EF    Whole-genome random sequencing and assembly of Haemophilus influenzae  Rd Science 1995 269 496 512 7542800 
Galtier N  Gouy M  Gautier C   SEAVIEW and PHYLO_WIN: Two graphic tools for sequence alignment and molecular phylogeny Comput Appl Biosci 1996 12 543 548 9021275 
Gogarten JP  Doolittle WF  Lawrence JG   Prokaryotic evolution in light of gene transfer Mol Biol Evol 2002 19 2226 2238 12446813 
Goldman N  Anderson JP  Rodrigo AG   Likelihood-based tests of topologies in phylogenetics Syst Biol 2000 49 652 670 12116432 
Heidelberg JF  Eisen JA  Nelson WC  Clayton RA  Gwinn ML    DNA sequence of both chromosomes of the cholera pathogen Vibrio cholerae 
 Nature 2000 406 477 483 10952301 
Hillis DM  Pollock DD  McGuire JA  Zwickl DJ   Is sparse taxon sampling a problem for phylogenetic inference? Syst Biol 2003 52 124 126 12554446 
Jain R  Rivera MC  Lake JA   Horizontal gene transfer among genomes: The complexity hypothesis Proc Natl Acad Sci U S A 1999 96 3801 3806 10097118 
Jones DT  Taylor WR  Thornton JM   The rapid generation of mutation data matrices from protein sequences Comput Appl Biosci 1992 8 275 282 1633570 
Koski LB  Golding GB   The closest BLAST hit is often not the nearest neighbor J Mol Evol 2001 52 540 542 11443357 
Kumar S  Tamura K  Nei M   MEGA: Molecular Evolutionary Genetics Analysis, version 1.01 1993 The Pennsylvania State University, University Park, Pennsylvania. 
Lawrence JG  Ochman H   Amelioration of bacterial genomes: Rates of change and exchange J Mol Evol 1997 44 383 397 9089078 
May BJ  Zhang Q  Li LL  Paustian ML  Whittam TS    Complete genomic sequence of Pasteurella multocida  Pm70 Proc Natl Acad Sci U S A 2001 98 3460 3465 11248100 
McClelland M  Sanderson KE  Spieth J  Clifton SW  Latreille P    Complete genome sequence of Salmonella enterica  serovar Typhimurium LT2 Nature 2001 413 852 856 11677609 
Moran NA   Accelerated evolution and Muller's rachet in endosymbiotic bacteria Proc Natl Acad Sci U S A 1996 93 2873 2878 8610134 
Moran NA  Mira A   The process of genome shrinkage in the obligate symbiont, Buchnera aphidicola 
 Genome Biol 2001 2 12 Available: http://genomebiology.com/2001/2/12/research/0054  via the Internet 
Moya A  Latorre A  Sabater-Munoz B  Silva FJ   Comparative molecular evolution of primary (Buchnera ) and secondary symbionts of aphids based on two protein-coding genes J Mol Evol 2002 55 127 137 12107590 
Nelson KE  Clayton RA  Gill SR  Gwinn ML  Dodson RJ    Evidence for lateral gene transfer between Archaea and bacteria from genome sequence of Thermotoga maritima 
 Nature 1999 399 323 329 10360571 
Nesbø CL  Boucher Y  Doolittle WF   Defining the core of nontransferable prokaryotic genes: The euryarchaeal core J Mol Evol 2001 53 340 350 11675594 
Ochman H  Jones IB   Evolutionary dynamics of full genome content in Escherichia coli 
 EMBO J 2000 19 6637 6643 11118198 
Ochman H  Lawrence JG  Groisman EA   Lateral gene transfer and the nature of bacterial innovation Nature 2000 405 299 304 10830951 
Parkhill J  Wren BW  Thomson NR  Titball RW  Holden MTG    Genome sequence of Yersinia pestis , the causative agent of plague Nature 2001 413 523 527 [Year corrected in 10/23/03] 11586360 
Parkhill J  Dougan G  James KD  Thomson NR  Pickard D    Complete genome sequence of a multiple drug resistant Salmonella enterica  serovar Typhi CT18 Nature 2001 413 848 852 11677608 
Pedulla ML  Ford ME  Houtz JM  Karthikeyan T  Wadsworth C    Origins of highly mosaic mycobacteriophage genomes Cell 2003 113 171 182 12705866 
Perna NT  Plunkett G  Burland V  Mau B  Glasner JD    Genome sequence of enterohaemorrhagic Escherichia coli  O157:H7 Nature 2001 409 529 533 11206551 
Schmidt HA  Strimmer K  Vingron M  von Haeseler A   TREE-PUZZLE: Maximum likelihood phylogenetic analysis using quartets and parallel computing Bioinformatics 2002 18 502 504 11934758 
Shigenobu S  Watanabe H  Hattori M  Sakaki Y  Ishikawa H   Genome sequence of the endocellular bacterial symbiont of aphids Buchnera  sp. APS Nature 2000 407 81 86 10993077 
Shimodaira H  Hasegawa M   Multiple comparisons of log-likelihoods with applications to phylogenetic inference Mol Biol Evol 1999 16 1114 1116 
Simpson AJG  Reinach FC  Arruda P  Abreu FA  Acencio M    The genome sequence of the plant pathogen Xylella fastidiosa : The Xylella fastidiosa  Consortium of the Organization for Nucleotide Sequencing and Analysis Nature 2000 406 151 157 10910347 
Singer GAC  Hickey DA   Nucleotide bias causes a genomewide bias in the amino acid composition of proteins Mol Biol Evol 2000 17 1581 1588 11070046 
Spaulding AW  von Dohlen CD   Phylogenetic characterization and molecular evolution of bacterial endosymbionts in psyllids (Hemiptera: Sternorrhyncha) Mol Biol Evol 1998 15 1506 1513 12572614 
Stover CK  Pham X-QT  Erwin AL  Mizoguchi SD  Warrener P    Complete genome sequence of Pseudomonas aeruginosa  PA01, an opportunistic pathogen Nature 2000 406 959 964 10984043 
Tatusov RL  Mushegian AR  Bork P  Brown NP  Hayes WS    Metabolism and evolution of Haemophilus influenzae  deduced from a whole-genome comparison with Escherichia coli 
 Curr Biol 1996 6 279 291 8805245 
Thompson JD  Higgins DG  Gibson TJ   CLUSTALW: Improving the sensitivity of progressive multiple sequence alignment through sequence weighting, positions-specific gap penalties and weight matrix choice Nucleic Acids Res 1994 22 4673 4680 7984417 
Tomii K  Kanehisa M   A comparative analysis of ABC transporters in complete microbial genomes Genome Res 1998 8 1048 1059 9799792 
Ueda K  Seki T  Kudo T  Yoshida T  Kataoka M   Two distinct mechanisms cause heterogeneity of 16S rRNA J Bacteriol 1999 181 78 82 9864315 
van Ham RCHJ  Moya A  Latorre A   Putative evolutionary origin of plasmids carrying the genes involved in leucine biosynthesis in Buchnera aphidicola  (endosymbiont of aphids) J Bacteriol 1997 179 4768 4777 9244264 
Woese CR   Bacterial evolution Microbiol Rev 1987 51 221 271 2439888 
Wolanin PM  Thomason PA  Stock JB   Histidine protein kinases: Key signal transducers outside the animal kingdom Genome Biol 2002 3 10 Available: http://genomebiology.com/2002/3/10/REVIEWS/3013  via the Internet 
Wolf YI  Rogozin IB  Grishin NV  Koonin EV   Genome trees and the tree of life Trends Genet 2002 18 472 479 12175808 
Xie G  Bonner CA  Brettin T  Gottardo R  Keyhani NO    Lateral gene transfer and ancient paralogy of operons containing redundant copies of tryptophan-pathway genes in Xylella  species and in heterocystous cyanobacteria Genome Biol 2003 4 2 Available: http://genomebiology.com/2003/4/2/R14  via the Internet 
Yap WH  Zhang Z  Wang Y   Distinct types of rRNA operons exist in the genome of the actinomycete Thermomonospora chromogena  and evidence for horizontal transfer of an entire rRNA operon J Bacteriol 1999 181 5201 5209 10464188 
Zhaxybayeva O  Gogarten JP   Bootstrap, Bayesian probability and maximum likelihood mapping: Exploring new tools for comparative genome analyses BMC Genomics 2002 3 4 Available: http://www.biomedcentral.com/1471–2164/3/4  via the Internet 
Zwickl DJ  Hillis DM   Increased taxon sampling greatly reduces phylogenetic error Syst Biol 2002 51 588 598 12228001

PMID: 0
Accession ID: PMC193606
License: CC BY
Last Updated: 2021-01-05 08:21:04
Retracted: no
Citation: PLoS Biol. 2003 Oct 15; 1(1):e23
==== Front
PLoS BiolPLoS BiolpbioplosbiolPLoS Biology1544-91731545-7885Public Library of Science San Francisco, USA 10.1371/journal.pbio.0000023SynopsisCell BiologyDevelopmentGenetics/Genomics/Gene TherapyMolecular Biology/Structural BiologyNeurosciencePhysiologyDrosophilaBiological Clock Depends on Many Parts Working Together Synopsis10 2003 15 9 2003 15 9 2003 1 1 e23Copyright: © 2003 Public Library of Science.2003This is an open-access article distributed under the terms of the Creative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are properly credited.

Drosophila Free-Running Rhythms Require Intercellular Communication
==== Body
How do people subjected to the endless dark days of winter in the far northern latitudes maintain normal daily rhythms? Though many might feel like hibernating, a highly regulated internal system keeps such impractical yearnings in check. From fruit flies to humans, nearly every living organism depends on an internal clock to regulate basic biological cycles such as sleep patterns, metabolism, and body temperature. And that clock runs on similar molecular mechanisms.

Specific clusters of neurons in the brain are known to control the biological clock. Scientists believed these brain “clock cells” function as independent units. But new research described in this issue shows that the neurons do not act in isolation; rather, they collaborate with other neurons in a cell-communication network to sustain the repeating circadian rhythm cycles.

Clock cells within the brain maintain an organism's circadian rhythms, even in the absence of cyclical environmental signals like light, in a state scientists call “free running.” Though it has long been clear that the circadian rhythms of an organism persist under such free-running conditions (for example, constant darkness), it was thought that the gene-expression patterns within the cells governing these biorhythms did not require any external, or extracellular, signals to continue ticking. In experiments described here, Michael Rosbash and his colleagues show that the key brain clock cells in fruit flies (Drosophila), called ventral lateral neurons, do indeed support the fly's circadian rhythms during periods of constant darkness and that the molecular expression patterns associated with these rhythms continue to cycle as well within other clock cells. These sustained expression patterns, however, require intercellular communication between different groups of brain clock cells.

In other words, the ventral lateral neurons do not act alone. When the molecular clock machinery was manipulated so that only the ventral lateral neurons were active, the fly's circadian rhythms were not sustained, suggesting the rhythms depend on other neuronal groups as well. The researchers also demonstrate that the persistence of normal cycling during constant darkness depends on a protein (called PDF) secreted by the ventral lateral cells.

The PDF neuropeptide protein was thought to connect the molecular expression pattern of the ventral lateral neurons with the manifestation of circadian rhythms, but the researchers found evidence of a larger influence. When mutant flies lacking a functional PDF gene were exposed to constant darkness, the molecular expression patterns gradually stopped. The scientists say this suggests that the ventral lateral neurons and the PDF protein it produces help coordinate the entire neural network that underlies circadian rhythms.


Drosophila lateral neuron (green)

PMID: 0
Accession ID: PMC193607
License: CC BY
Last Updated: 2021-01-05 08:21:04
Retracted: no
Citation: PLoS Biol. 2003 Oct 15; 1(1):e31
==== Front
PLoS BiolPLoS BiolpbioplosbiolPLoS Biology1544-91731545-7885Public Library of Science San Francisco, USA 10.1371/journal.pbio.0000031SynopsisEvolutionGenetics/Genomics/Gene TherapyMicrobiologyEubacteriaNew Genomic Approach Predicts True Evolutionary History of Bacterial Genomes Synopsis10 2003 15 9 2003 15 9 2003 1 1 e31Copyright: © 2003 Public Library of Science.2003This is an open-access article distributed under the terms of the Creative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are properly credited.
From Gene Trees to Organismal Phylogeny in Prokaryotes: The Case of the γ-Proteobacteria
==== Body
Bacteria are an indiscriminate lot. While most organisms tend to pass their genes on to the next generation of their species, bacteria often exchange genetic material with totally unrelated species. That is why skeptics doubted that bacteria researchers could ever hope to map a reliable history of cell lineages in bacteria over time. But now, thanks to the availability of sequenced genomes for groups of related bacteria, researchers at the University of Arizona demonstrate that constructing a bacterial family tree is indeed possible.

Previous efforts to trace the ancestry of bacteria were constrained by a dearth of related bacterial genomes, which, among other things, prevented scientists from successfully accounting for bacteria's tendency to exchange genes with unrelated organisms. In this process, called lateral gene transfer, organisms acquire genetic material not from their ancestors, the most prevalent route, but from unrelated organisms. Lateral gene transfer greatly complicates the issue of who descended from whom, because two organisms could appear closely related based on the similarity of some genes but distantly related based on other genes. The problem is to determine which genes have been faithfully vertically transmitted—from parent cell to offspring—and thus reflect the history of the bacterial cell lineages.

In this issue, Nancy Moran, Emmanuelle Lerat, and Vincent Daubin propose an approach that solves this problem by identifying a set of genes that serve as reliable indicators of the vertical transfer of bacterial cell lineages. This method has important implications for biologists studying the evolutionary history of organisms by establishing a foundation for charting the evolutionary events, such as lateral gene transfer, that shape the structure and substance of genomes. With this method, scientists can begin to understand how bacteria have evolved and how their genomes have changed.

Bacteria promise to reveal the most information about genomic evolution, because so many clusters of related bacterial genomes have been sequenced—allowing for broad comparative analysis among species—and their genomes are small and relatively compact. In this study, the researchers chose the ancient bacteria group Proteobacteria, an ecologically diverse group (including Escherichia coli and Salmonella species) with the most documented cases of lateral gene transfer and the highest number of species with sequenced genomes.

The researchers identified a set of likely single-copy orthologs (homologous genes that diverged due to the speciation of ancestral lineages) with widespread distribution in the different species of Proteobacteria that could be used to trace the history of the cell lineages. Surprisingly, they found that almost all of the 205 ortholog gene families they selected supported the same evolutionary branching pattern. Only two did not, which the researchers then investigated and found to be the result of lateral gene transfer.

These results, the researchers say, support the ability of their method to reconstruct the important evolutionary events affecting genomes. By mapping out the evolutionary path of genetic information on a genomic level, their approach promises to elucidate not only the evolution of bacterial genomes but also the diversification of species.

Electron micrograph of Proteobacteria in eukaryotic cell

PMID: 12969509
Accession ID: PMC212319
License: CC BY
Last Updated: 2022-01-04 23:15:02
Retracted: no
Citation: BMC Cell Biol. 2003 Sep 11; 4:13
==== Front
BMC Cell Biol
BMC Cell Biol
BMC Cell Biology
1471-2121
BioMed Central London

12969509
72
10.1186/1471-2121-4-13
Research Article
The Guanine Nucleotide Exchange Factor ARNO mediates the activation of ARF and phospholipase D by insulin
Li Hai-Sheng hal9001@pitt.edu

1
Shome Kuntala shome@pitt.edu

1
Rojas Raúl rerst14@pitt.edu

12
Rizzo Megan A MRizzo@som.umaryland.ed

1
Vasudevan Chandrasekaran cvasudevan@cellomics.com

1
Fluharty Eric erf3@pitt.edu

1
Santy Lorraine C ls6e@virginia.edu

3
Casanova James E jec9e@virginia.edu

3
Romero Guillermo ggr@pitt.edu

1
1 grid.21925.3d 0000000419369000 Departments of Pharmacology, University of Pittsburgh School of Medicine, Pittsburgh, PA 15261 USA
2 grid.21925.3d 0000000419369000 Cell Biology and Physiology, University of Pittsburgh School of Medicine, Pittsburgh, PA 15261 USA
3 grid.27755.32 000000009136933X Department of Cell Biology, University of Virginia School of Medicine, Charlottesville, VA 22908 USA
11 9 2003
11 9 2003
2003
4 1309 7 2003
11 9 2003
© Li et al; licensee BioMed Central Ltd. 2003, This article is published under license to BioMed Central Ltd. This is an Open Access article: verbatim copying and redistribution of this article are permitted in all media for any purpose, provided this notice is preserved along with the article's original URL.
https://creativecommons.org/licenses/by/4.0/ This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.The Creative Commons Public Domain Dedication waiver (http://creativecommons.org/publicdomain/zero/1.0/) applies to the data made available in this article, unless otherwise stated in a credit line to the data.
Background

Phospholipase D (PLD) is involved in many signaling pathways. In most systems, the activity of PLD is primarily regulated by the members of the ADP-Ribosylation Factor (ARF) family of GTPases, but the mechanism of activation of PLD and ARF by extracellular signals has not been fully established. Here we tested the hypothesis that ARF-guanine nucleotide exchange factors (ARF-GEFs) of the cytohesin/ARNO family mediate the activation of ARF and PLD by insulin.

Results

Wild type ARNO transiently transfected in HIRcB cells was translocated to the plasma membrane in an insulin-dependent manner and promoted the translocation of ARF to the membranes. ARNO mutants: ΔCC-ARNO and CC-ARNO were partially translocated to the membranes while ΔPH-ARNO and PH-ARNO could not be translocated to the membranes. Sec7 domain mutants of ARNO did not facilitate the ARF translocation. Overexpression of wild type ARNO significantly increased insulin-stimulated PLD activity, and mutations in the Sec7 and PH domains, or deletion of the PH or CC domains inhibited the effects of insulin.

Conclusions

Small ARF-GEFs of the cytohesin/ARNO family mediate the activation of ARF and PLD by the insulin receptor.

Electronic supplementary material

The online version of this article (doi:10.1186/1471-2121-4-13) contains supplementary material, which is available to authorized users.

Keywords

Insulin Receptor
Digitonin
Insulin Stimulation
Sec7 Domain
Human Insulin Receptor
issue-copyright-statement© The Author(s) 2003
==== Body
pmcBackground

Small GTPases of the ADP-ribosylation factor (ARF) family play a major role in membrane trafficking in eukaryotic cells [1]. ARF activation is facilitated by specific guanine nucleotide exchange factors (ARF-GEFs). Several ARF-GEFs have been identified, varying in size, structure and subcellular distribution [2–6]. Of particular interest in signaling events are the members of the cytohesin/ARNO family of ARF-GEFs. These proteins have been found to associate with the plasma membrane under certain conditions, and consist of three well-defined motifs: an N-terminal coiled-coil domain (CC domain), a central domain with homology to the yeast protein Sec7 (Sec7 domain), and a C-terminal pleckstrin homology domain (PH domain) (Fig. 1). The catalytic activity of ARNO for guanine nucleotide exchange is localized in the Sec7 domain and appears to be regulated through the interaction of the PH domain with phosphatidylinositol (PtdIns) (3,4,5)-P3 [7, 8], an intermediate in signaling cascades regulated by insulin and other agonists [3].Figure 1 Schematic structure of ARNO constructs. Full length of wild type ARNO and ΔPH-ARNO were subcloned either in pCMV-myc or pEGFP-C1. PH-ARNO and ΔCC-ARNO were subcloned in pEGFP-C1. CC-ARNO was subcloned in pEGFP-N1.

Phospholipase D (PLD) catalyzes the hydrolysis of phosphatidylcholine (PC) to produce phosphatidic acid (PA). It is involved in a variety of signaling pathways and membrane traffic processes [9, 10]. Many hormones, neurotransmitters, and growth factors, including insulin, have been shown to induce the activation of PLD [11, 12]. Several factors are involved in the regulation of cellular PLD activity, such as Ca2+, protein kinase C, tyrosine kinases, and G proteins [13–17]. Among these, the members of the ARF and Rho families of GTPases appear to be the most potent physiological activators [18–24]. However, the mechanism of the activation of PLD by ARF and Rho has not yet been fully established.

This study was designed to investigate the role of ARNO in the regulation of PLD activity by insulin in HIRcB cells, a Rat-1 fibroblast cell line that overexpresses human insulin receptors. The objectives were: 1) to test if insulin induces the translocation of wild type ARNO to the plasma membrane in transiently transfected HIRcB cells; 2) to determine whether ARNO translocation is accompanied by activation and subcellular translocation of ARF; 3) to explore if overexpression of wild type ARNO in HIRcB cells alters insulin-dependent PLD activity; and 4) to investigate the function of individual domains of ARNO in insulin-dependent PLD and ARF activation.

Results

Insulin–dependent binding of ARNO to cell membranes

The translocation of ARNO and ARNO mutants to the membranes was studied in HIRcB cells using a digitonin permeabilization assay. For these experiments, HIRcB cells were transiently transfected with myc-tagged wild type ARNO and the following mutants: ΔPH-ARNO, PH-ARNO, ΔCC-ARNO, CC-ARNO, E156K-ARNO and R280D-ARNO. This assay is based on the formation of pores in the plasma membrane induced by digitonin to allow cytosolic proteins to leak out of treated cells upon centrifugation. Fig. 2 shows that, after digitonin permeablization, a significant fraction of ARNO proteins leaked out of serum-starved HIRcB cells that transiently overexpressed the wild type ARNO and its mutants. Since these proteins were mostly recovered from the supernatant fractions, suggesting that wild type ARNO and the mutants tested are predominantly cytosolic in non-stimulated cells. In contrast, when digitonin permeablization was performed in the presence of insulin (100 nM), most of wt-ARNO, E156K-ARNO, and ΔCC-ARNO as well as a part of CC-ARNO were recovered from the particulate membrane fraction, suggesting that these ARNO proteins can be recruited to the membrane by insulin to various degrees. However, neither R280D-ARNO nor ΔPH-ARNO was recovered from the particulate fraction after insulin stimulation, suggesting that the translocation of ARNO to the membrane requires an intact PH-domain. It should be noted that, although the CC domain alone binds to the membranes under stimulation conditions, the degree of the binding is much less than that of wild type ARNO (Fig. 2). Surprisingly, a construct containing only the PH domain of ARNO could not be recruited to the membranes by insulin, indicating that the PH domain is essential but not sufficient for the translocation of ARNO.Figure 2 Insulin promotes the translocation of ARNO to cell membranes. HIRcB cells were transfected with myc-wt-ARNO, myc-E156K-ARNO, myc-R280D-ARNO, myc-ΔPH-ARNO, EGFP-PH-ARNO, EGFP-ΔCC-ARNO, and CC-ARNO-EGFP. The cells were treated with/without (Control) 10 μM digitonin (Dig). Where indicated, 100 nM insulin, 1 mM ATP, and 100 μM GTPγS were present during permeablization reaction. Pellets and supernatants were separated by centrifugation and the presence of myc-ARNO and its mutants or ARNO-EGFP in each fraction was determined by immunoblotting.

ARNO recruits ARF1 to the plasma membrane in an insulin-dependent manner

Since ARNO is an activation factor of ARF, we tested the hypothesis that agonist-dependent ARNO translocation facilitates the local binding of ARF proteins to the membrane. An initial set of real-time studies was done using HeLa cells that had been stably transfected with an ARF1-GFP construct [25]. These cells were transfected with myc-ARNO, serum-starved overnight, and imaged with a confocal microscope equipped with a constant-temperature microperfusion incubator to maintain the temperature at 37°C. Time-lapse images were collected at 30-second intervals. A representative experiment was shown in Fig. 3A. Prior to insulin stimulation, ARF1-GFP protein was mostly cytosolic or bound to the Golgi apparatus, although a small amount of ARF-GFP was localized on the surface of the cells. Ten minutes after the insulin stimulation, most of the ARF1-GFP was found on the plasma membrane. Similar results were obtained with HIRcB cells co-transfected with ARNO-myc and ARF1-GFP (Fig. 3B). It should be noted that a significant accumulation of ARF1-GFP on the plasma membrane was not observed in the cells that had not been transfected with ARNO (not shown), or that had been transfected with the inactive mutant E156K-ARNO (Fig. 3B). Since the endogenous levels of ARNO in HeLa cells were so low that the protein could not be detected in Western blots, it is reasonable to assume that under physiological conditions only a very small fraction of ARF1 translocates to the plasma membrane in response to extracellular agonists.Figure 3 A. Real time image of the translocation of ARF1-GFP to the plasma membrane. HeLa cells that had been stably transfected with ARF1-GFP were transiently transfected with myc-ARNO, serum starved overnight, and treated with 100 nM insulin. Images were collected every 30 seconds using a Molecular Dynamics 2001 confocal microscope. The time intervals that were indicated on the upper right hand corner of each panel represent the time after the addition of insulin. B. The translocation of ARF1-GFP to the plasma membrane by the effects of insulin requires ARNO. ARF1-GFP/HeLa cells were transfected with myc-ARNO, treated, fixed, and stained for myc-epitope as described in the Materials and Methods section. Images displaying ARF1-GFP (green) and myc-ARNO (red) were merged us ing Adobe Photoshop software.

ARNO interacts directly with the insulin receptor

Our previous work has shown that the insulin receptor co-immunoprecipitates with ARF in an agonist-dependent manner [23]. Furthermore, we have also shown that an ARF-GEF activity is associated with the insulin receptor and that this activity is not a function of the receptor itself [23]. Given that many receptor tyrosine kinases form complexes with their target proteins, we tested the hypothesis that ARNO binds the insulin receptor.

Figure 4 shows that insulin receptors that were immunoprecipitated in the presence of insulin were associated with an ARF-GEF activity (Fig 4 ●), and that the ARF-GEF activity that was co-immunoprecipitated with the insulin receptor was significantly increased in the cells that had been transiently transfected with myc-ARNO (Fig. 4 ■). Insulin receptors that were immunoprecipitated in the absence of insulin did not accelerate the binding of GTPγS to the recombinant ARF1 as much as those obtained in the presence of insulin (Fig. 4 ○), indicating that the association of ARF-GEF activity with the insulin receptor was dependent on the presence of insulin.Figure 4 The ARF-GDP exchange activity of the coimmunoprecipitates with the insulin receptor. The exchange activity was determined as described in Materials and Methods. (○,□) Receptors were immunoprecipitated in the absence of insulin from cells transfected with empty vector (○) or with myc-ARNO (□). (●,■) Receptors were immunoprecipitated in the presence of insulin from cells transfected with empty vector (●) or with myc-ARNO (■).

We then transfected HIRcB cells with myc-tagged ARNO constructs. Fig. 5 shows that the wild type ARNO co-immunoprecipitated with the insulin receptor in an insulin-dependent manner. E156K-ARNO was also co-immunoprecipitated with the insulin receptor upon insulin stimulation. However, none of the deletion mutants, including ΔPH-ARNO, PH-ARNO, ΔCC-ARNO, and CC-ARNO, as well as a site-directed mutant R280D-ARNO, was found co-immunoprecipitated with the insulin receptor. These data suggest that ARNO directly interacts with the insulin receptor and that the interaction requires intact PH and CC domains, but the catalytic activity of the Sec7 domain does not alter the interaction.Figure 5 Immunoprecipitation of the insulin receptor with ARNO and its mutants. Immunoprecipitated proteins were resolved by SDS-PAGE and myc-ARNO, myc-E156K-ARNO, myc-R280D-ARNO and myc-ΔPH-ARNO were detected by immunoblotting with a monoclonal anti-myc epitope antibody. PH-ARNO-EGFP, ΔCC-ARNO-EGFP, and CC-ARNO-EGFP were detected by immunoblotting with a polyclonal antibody against EGFP.

Effects of the overexpression of ARNO or its mutants on insulin-dependent PLD activity

We have shown so far that ARNO mediates the translocation of ARF proteins to the plasma membrane with insulin stimulation. Since ARF proteins mediate the activation of PLD by insulin [23], we tested the hypothesis that ARNO may play a role in the regulation of PLD activitiy upon insulin stimulation. To prove this point, the PLD activity of HIRcB cells that had been transiently transfected with the wild type ARNO, and mutant ARNO constructs.

Fig. 6 shows that the overexpression of the wild type ARNO significantly increased insulin-induced PLD activity when compared with that of non-transfected cells. In contrast, the overexpression of the indicated ARNO mutants significantly decreased the ability of insulin to stimulate PLD. We conclude, therefore, that members of the cytohesin/ARNO family of ARF GEFs play an important role in the regulation of PLD activity by insulin.Figure 6 Effects of overexpression of the wild type and mutant ARNO constructs on the activation of phospholipase D by insulin. HIRcB cells were trans fected with empty vector, myc-wt-ARNO, myc-E156K-ARNO, myc-R280D-ARNO, and myc-ΔPH ARNO, PH-ARNO-EGFP, ΔCC-ARNO-EGFP, and CC-ARNO-EGFP. PLD activity was determined by a transphosphatidylation assay as described in Materials and Methods.

Discussion

Several studies have demonstrated that ARF proteins may mediate receptor-dependent activation of PLD. Stimulation of cell surface receptors with agonists, such as insulin, promotes the translocation of ARF proteins to the cell membranes and the activation of ARF proteins and the subsequent activation of PLD [16, 18, 21, 23]. However, the mechanisms by which ARF proteins are activated by cell surface receptors remain obscure.

ARF GEFs of the cytohesin/ARNO family have been shown to be recruited to cell membranes by mechanisms that are influenced by extracellular agonists [7, 26]. These GEFs have been implicated in the regulation of many cellular processes, ranging from the regulation of cell motility [27] to cell adhesion [28] and, more recently, oncogenesis [29]. It has been speculated that PLD activation may mediate several of the cellular events regulated by cytohesin/ARNO GEFs [30]. However, a direct proof of a role for these factors in the regulation of the receptor-mediated PLD activation is still lacking. To address these and other related issues, we have studied in detail some of the mechanistic aspects of this pathway using a fibroblast cell line that overexpresses human insulin receptors as a model. This model and other similar ones have been used in our laboratory and others to examine specific aspects of insulin receptor function, such as receptor phosphorylation and traffic [23, 31–33] and the regulation of the MAPK pathway [34].

Our studies showed that insulin promoted the translocation of myc-tagged ARNO constructs to the plasma membrane. This result is in agreement with data previously published by Venkateswarlu et al [7] and Langille et al [35] who demonstrated the insulin-dependent translocation of ARNO and the related protein GRP-1 to the plasma membrane, respectively. A detailed analysis of ARNO deletion and point mutants demonstrated that: 1) the translocation of ARNO to the membrane is independent of its ARF-GEF activity; 2) ARNO translocation to the plasma membrane requires an intact PH domain; 3) the CC domain of ARNO plays a role in targeting ARNO to the plasma membrane; 4) neither the PH domain of ARNO nor its CC domain alone sufice to target the protein to the plasma membrane; and 5) the plasma membrane translocation of ARNO is strongly regulated by insulin and, perhaps, other extracellular agonists.

The linkage between ARNO translocation to specific subcellular fractions and ARF activation was studied using myc-tagged ARNO and ARF-GFP constructs in two different cell types. Our data showed conclusively that insulin promoted the co-localization of wild type myc-ARNO and ARF1-GFP on the surface of HIRcB and HeLa cells. Interestingly, insulin, acting through ARNO, promoted the translocation of ARF1-GFP to the plasma membrane. ARF1, like most members of the ARF family, is primarily a cytosolic protein that exerts its function on specific membranes to which it is recruited by specific activators that promote the binding of GTP. However, ARF1 seems to act primarily at the Golgi, promoting the binding of coatomer proteins to the Golgi membrane [36, 37]. Nevertheless, the fact remains that ARF1 is primarily cytosolic, and that only a small fraction of it is bound to the Golgi membrane at any time [36]. It is not surprising, therefore, that some ARF1 may bind to the plasma membrane after being locally activated by ARNO, which is in turn recruited to the cell surface by the action of insulin. It should be remembered that our cells overexpress ARF1-GFP. Whether ARF1 does in fact work at the plasma membrane under physiological conditions or not remains to be established. Our data simply establish the fact that a receptor-dependent mechanism to recruit ARF1 to the plasma membrane does exist. On the other hand, ARF6 is normally found associated with the plasma membrane [36, 38], and there is evidence that ARF6 might be the primary target for ARF-GEFs of the cytohesin/ARNO family [27]. However, when ARF dominant negative mutants were tested for their ability to inhibit agonist-dependent PLD activation, the data showed that ARF1 dominant negative mutants (T31N-ARF1) were as efficient as ARF6 mutants (T27N-ARF6) [23]. These observations strongly support the idea that ARF-GEFs of the cytohesin/ARNO family have full access to the cytosolic ARF proteins. Therefore, although ARF6 might be the primary intermediate for ARNO-regulated PLD activation, other ARF proteins may as well play an important role in the pathway.

The ability of insulin to promote the translocation of ARNO and ARF to the plasma membrane correlated well with the ability of insulin to promote the activation of PLD. Therefore, our data support the hypothesis that the activation of PLD by insulin is mediated by ARF-GEFs of the cytohesin/ARNO family by a mechanism that involves the interaction of the PH and CC domains of these GEFs with some specific cellular targets. This conclusion is based on the demonstration that ARNO constructs with catalytically inactive domain or the mutants with defective PH and CC domains acted as dominant inhibitors of insulin-dependent PLD activation. The dominant negative effects of E156K-ARNO were not unexpected, since this mutant contains the intact PH and the CC domains and is therefore likely to compete with endogenous ARNO. The dominant negative effect of the PH and the CC domain deletion mutants on PLD activation was of particular interest. These mutants were at best partially translocated to the membrane but blocked the ability of insulin to promote ARF and PLD activation. This result was somewhat surprising since these deletion mutants contain an intact Sec7 domain and, therefore, would have been expected to support ARF and PLD activity. However, this was not the case, suggesting that all regions of ARNO play an important role in the regulation of this protein. Moreover, the failure of the ΔCC mutant to activate ARF and PLD indicates that other cellular targets that bind to the CC doma in of ARNO and regulate the subcellular location or the function of the signaling protein complex may exist. In fact, some proteins that interact strongly with the CC domain of members of the ARNO family, such as CASP and GRASP, have already been identified [39, 40]. Consistent with these ideas was the observation that the overexpression of either the PH or the CC domain alone was sufficient to block insulin-dependent PLD activation. Therefore, we propose that cellular targets that recognize both the PH and CC domains of ARNO are important for the regulation of the function of this protein by cell surface receptors.

On the other hand, our data also strongly support the hypothesis that the regulation of ARNO activity by insulin involves, at least transiently, a direct interaction of the insulin receptor with ARNO. Consistently, the presence of an ARNO-like activity and ARNO in the immunoprecipitated materials was confirmed by biochemical experiments. Finally, ARNO constructs lacking either the CC or the PH domain, or with a defective PH domain, failed to co-immunoprecipitate with the insulin receptor. These findings suggest a mechanism of the activation in which the binding of ARNO to the membrane is regulated by the insulin receptor at two different levels: 1) ARNO must interact with the receptor; and 2) ARNO must interact with the membrane, either via binding to polyphosphoinositides or through the interaction with specific protein targets. Our data strongly support the idea that both CC and PH domains play a crucial role in this phenomenon.

Conclusions

This study suggests a general model for the activation of PLD with insulin stimulation. Insulin, upon binding to its receptor, promotes the phosphorylation of IRS-1 and the activation of PI3 kinase. This results in the accumulation of polyphosphoinositides on the plasma membrane. In parallel, the insulin-bound receptor promotes the recruitment of ARNO (and/or other members of the ARNO family, such as GRP-1) to the plasma membrane, either by direct interaction with their CC and PH domains or by promoting the interaction of ARNO with other as yet unidentified targets. The binding of ARF-GEFs to the plasma membrane is stabilized by the interactions of their PH domain with polyphosphoinositides generated by the action of PI3 kinase. Once on the membrane, the ARF-GEFs catalyze the activation of membrane-bound ARF6 or cytosolic ARF proteins that are then recruited to the membrane where they may activate PLD.

Cell culture

Rat-1 fibroblasts overexpressing the human insulin receptors (HIRcB cells) were cultured in Dulbecco's modified Eagle's medium (DMEM)/Ham's F-12, supplemented with 10% fetal bovine serum, antibiotics, and 100 nM methotrexate, as previously described [20]. Cells were subcultured, transfected as indicated in the figure legends, and serum starved for overnight (approximately 20 hrs) prior to insulin stimulation.

HeLa cells were cultured in DMEM supplemented with 10% fetal bovine serum and antibiotics. HeLa-ARF1-GFP stable transfectants were obtained by using G418 as a selection agent as described elsewhere [25]. Clonal populations were obtained and used in the assays described here.

Transient Transfection

Subconfluent (70–90%) HIRcB cells were transfected with LipofectAMINE (Invitrogen) for biochemical analyses or Superfect (QIAGEN) for imaging analyses. Transfection was performed according to the manufacturer's instructions. Transfection efficiencies were 70–90% for LipofectAMINE and 40–50% for Superfect transfection reagent as previously described [41].

Generation of fusion proteins

It has been reported that the members of the cytohesin/ARNO family of ARF-GEFs each exist in two isoforms in terms of existence of extra G (glycine) in PH domain [42]. In this study, we used the isoform of ARNO with GGG (tri-glycine), which has similar binding affinities for both PI-(3,4,5)-P3 and PI-(4,5)-P3. The following myc-tagged ARNO constructs were generated: wt-ARNO, ΔPH-ARNO, PH-ARNO, ΔCC-ARNO, E156K-ARNO, and R250D-ARNO. wt-ARNO, ΔPH-ARNO (amino acids 1 to 269), PH-ARNO (amino acids 262–399), and ΔCC-ARNO (amino acids 51–399) (Fig. 1) were amplified by PCR and subcloned in the multiple cloning site of the vector pEGFP-C1 (CLONTECH) and fused to green fluorescent protein (GFP) as described by Venkateswarlu and coworkers [7]. The CC domain of ARNO (amino acids 1 to 55) (Fig. 1) was PCR out of wt-ARNO and subcloned into pEGFP-N1 using BglII and EcoRI restriction sites. E156K-ARNO (inactive Sec7 domain) was generated by site-directed mutagenesis as described by Frank and coworkers [43]. R280D-ARNO was designed on the basis of that a mutation on an analogous arginine impairs the binding of cytohesin-1 to polyphosphoinositides [26]. The sequences of the constructs were verified by direct sequencing and the expression of appropriate fusion proteins was examined by Western blotting. The level of expression of all constructs was found to be comparable.

Immunoprecipitation assay

Transfected and serum-starved HIRcB cells were washed with ice-cold PBS, scraped, and collected by centrifugation. The cell pellets were solubilized on ice for 1 hr in a solution of 50 mM Hepes, pH 7.45, containing 100 mM NaCl, 1.5% sodium cholate, 1 mM EDTA, 1 mM EGTA, 5 ug/ml leupeptin, 1 mM PMSF, and 1 mg/ml soybean trypsin inhibitor. Insoluble materials were removed by centrifugation. The cell lysate was immunoprecipitated with anti-mouse IgG agarose that had been equilibrated with a monoclonal antibody 83.7 (which recognizes the α subunit of the human insulin receptor). Immunoprecipitation was carried out overnight (approximately 20 hrs) at 4°C. The immunoprecipitates were washed with lysis buffer, resuspended in SDS-PAGE sample buffer, and subjected to Western blotting analysis.

Immunoblotting

Proteins were separated by SDS-PAGE, transferred to a nitrocellulose membrane, and blocked with 5% non-fat milk in PBS containing 0.1% Tween at room temperature for 2 hrs. The membrane was then cut in half horizontally. The upper part was used to detect the β subunit of the insulin receptor with a monoclonal antibody, CT-1, that recognizes the carboxyl terminus of the β subunit of the human insulin receptor. The lower part was used to detect ARNO proteins with a monoclonal antibody anti-myc or a polyclonal antibody anti-GFP.

PLD activity assay

Serum-starved HIRcB cells were labeled overnight with 3H-palmitate (5 μCi/ml) in serum-free medium. The cells were stimulated with insulin (100 nM) in the presence of 0.5–1% ethanol for 20 min. The reaction was stopped by addition of chloroform: methanol (1:1). The lipid phase was extracted and developed by thin layer chromatography (TLC) on silica gel 60 plates using ethyl acetate: trimethylpentane: acetic acid (9: 5: 2) as a solvent. The position of major phospholipids was determined using true standards (Avanti Biochemicals) and autoradiography. The TLC plates were scraped and the total amount of radioactivity associated with each lipid species was determined by liquid scintillation counting. The data were expressed as the number of counts associated with the phosphatidylethanol (PtdEtOH) spot normalized by the total number of counts of lipid.

Digitonin treatment

Serum-starved HIRcB cells were collected, resuspended in PBS, and treated with 10 μM digitonin in the presence or absence of insulin (100 nM), ATP (1 mM), and GTPγS (100 μM) at 37°C for 15 min. To release intracellular proteins, the digitonin-treated cells were centrifuged in a microcentrifuge for 20 min. The supernatants and the cell pellets were collected separately, and subjected to SDS-PAGE. ARNO proteins were detected by immunoblotting as described above.

In vitro ARF activation assay

ARF activation was determined by the binding of GTPγS to the purified, myristoylated recombinant human ARF1 (mhARF1), as described by Shome and coworkers [23]. The insulin receptor was immunoprecipitated in the presence or absence of 100 nM insulin as described above. Four to 8 μg mhARF1 and the immunoprecipitated insulin receptors were incubated with 100 nM GTPγ[35S] (1 μCi) in 20 mM Hepes buffer containing 2 mM MgCl2/ 0.1% Na-cholate / 1 mM ATP. At the indicated time points, the reaction was quenched by addition of 100 μM ice-cold, unlabeled GTPγS and the protein-bound nucleotide was determined by filtration through nitrocellulose filters as described [23].

Confocal microscopy

HIRcB cells were plated on poly-L-lysine coated glass coverslips and transfected with the constructs as indicated above. Cells were serum starved overnight and stimulated with 100 nM insulin. Live cells were imaged in a LSM5 Zeiss laser scanning confocal microscope equipped with a 63X oil immersion objective.

For ARF and ARNO colocalization experiments, HIRcB cells were plated on poly-L-lysine coated coverslips as described above and co-transfected with myc-ARNO and ARF-GFP constructs using Superfect transfection reagent according to the manufacturer's instructions. Following insulin stimulation, the cells were fixed with 4% fresh paraformaldehyde in PBS at 4°C for 30 min, and permeabilized in 0.1% Triton X-100 at room temperature for 2 min. After permeabilization, the cells were blocked with 3% bovine serum albumin in PBS at room temperature for 30 min, and immunostained with a monoclonal antibody 9E10 (Upstate Biotechnology) that recognizes the myc epitope. After extensively washing, the cells were incubated with a Cy5-conjugated donkey anti-mouse secondary antibody (Jackson Immunoresearch) and imaged using a Zeiss laser scanning confocal microscope with filters appropriate for the detection of GFP and Cy5.

Authors’ original submitted files for images

Below are the links to the authors’ original submitted files for images.Authors’ original file for figure 1

Authors’ original file for figure 2

Authors’ original file for figure 3

Authors’ original file for figure 4

Authors’ original file for figure 5

Authors’ original file for figure 6

Acknowledgement

This research was supported by the NIH (R01 DK 51183 and R01 DK 54782). GR is a recipient of an independent investigator Award from NIDDK (K02 DK02465). MAR and RR were supported by NIH pre-Doctoral Training Grant 5T32-GM08424. CV was supported by a Grant from the American Heart Association (PA Affiliate).

Authors' contributions

Kuntala Shome carried out some in vitro ARF activation, ARNO translocation and PLD assays. Raúl Rojas contributed with the initial studies of ARNO/ARF translocation. Megan Rizzo and Chandrasekaran Vasudevan performed most of the color imaging studies. Eric Fluharty, Lorraine C Santy and James Casanova made ARNO mutants. Hai-Sheng Li made a CC-ARNO mutant; carried out imaging analysis; and participated in the ARNO/ARF translocation and PLD assays. Guillermo Romero coordinated the study and participated in the imaging studies.
==== Refs
References

1. Moss J Vaughan M Molecules in the ARF orbit J Biol Chem 1998 273 21431 21434 9705267
2. Chardin P Paris S Antonny B Robineau S Beraud-Dufour S Jackson CL Chabre M A human exchange factor for ARF contains Sec7- and pleckstrin-homology domains Nature 1996 384 481 484 8945478
3. Klarlund JK Guilherme A Holik JJ Virbasius JV Chawla A Czech MP Signaling by phosphoinositide -3,4,5-trisphosphate through proteins containing pleckstrin and Sec7 homology domains Science 1997 275 1927 1930 9072969
4. Meacci E Tsai SC Adamik R Moss J Vaughan M Cytohesin-1, a cytosolic guanine nucleotide-exchange protein for ADP-ribosylation factor Proc Natl Acad Sci U S A 1997 94 1745 1748 9050849
5. Morinaga N Moss J Vaughan M Cloning and expression of a cDNA encoding a bovine brain brefeldin A-sensitive guanine nucleotide-exchange protein for ADP-ribosylation factor Proc Natl Acad Sci U S A 1997 94 12926 12931 9371777
6. Peyroche A Paris S Jackson CL Nucleotide exchange on ARF mediated by yeast Gea1 protein Nature 1996 384 479 481 8945477
7. Venkateswarlu K Oatey PB Tavare JM Cullen PJ Insulin-dependent translocation of ARNO to the plasma membrane of adipocytes requires phosphatidylinositol 3-kinase Curr Biol 1998 8 463 466 9550703
8. Venkateswarlu K Gunn-Moore F Oatey PB Tavare JM Cullen PJ Nerve growth factor- and epidermal growth factor-stimulated translocation of the ADP-ribosylation factor-exchange factor GRP1 to the plasma membrane of PC12 cells requires activation of phosphatidylinositol 3-kinase and the GRP1 pleckstrin homology domain Biochem J 1998 335 Pt 1 139 146 9742223
9. Bi K Roth MG Ktistakis NT Phosphatidic acid formation by phospholipase D is required for transport from the endoplasmic reticulum to the Golgi complex Curr Biol 1997 7 301 307 9133344
10. Ktistakis NT Brown HA Sternweis PC Roth MG Phospholipase D is present on Golgi-enriched membranes and its activation by ADP ribosylation factor is sensitive to brefeldin A Proc Natl Acad Sci U S A 1995 92 4952 4956 7761430
11. Billah MM Phospholipase D and cell signaling Curr Opin Immunol 1993 5 114 123 8383981
12. Exton JH Phosphatidylcholine breakdown and signal transduction Biochim Biophys Acta 1994 1212 26 42 8155724
13. Colley WC Sung TC Roll R Jenco J Hammond SM Altshuller Y Bar-Sagi D Morris AJ Frohman MA Phospholipase D2, a distinct phospholipase D isoform with novel regulatory properties that provokes cytoskeletal reorganization Curr Biol 1997 7 191 201 9395408
14. Hammond SM Altshuller YM Sung TC Rudge SA Rose K Engebrecht J Morris AJ Frohman MA Human ADP-ribosylation factor-activated phosphatidylcholine-specific phospholipase D defines a new and highly conserved gene family J Biol Chem 1995 270 29640 29643 8530346
15. Lopez I Arnold RS Lambeth JD Cloning and initial characterization of a human phospholipase D2 (hPLD2). ADP-ribosylation factor regulates hPLD2 J Biol Chem 1998 273 12846 12852 9582313
16. Sung TC Altshuller YM Morris AJ Frohman MA Molecular analysis of mammalian phospholipase D2 J Biol Chem 1999 274 494 502 9867870
17. Sung TC Zhang Y Morris AJ Frohman MA Structural analysis of human phospholipase D1 J Biol Chem 1999 274 3659 3666 9920915
18. Fensome A Whatmore J Morgan C Jones D Cockcroft S ADP-ribosylation factor and Rho proteins mediate fMLP-dependent activation of phospholipase D in human neutrophils J Biol Chem 1998 273 13157 13164 9582356
19. Karnam P Standaert ML Galloway L Farese RV Activation and translocation of Rho (and ADP ribosylation factor) by insulin in rat adipocytes. Apparent involvement of phosphatidylinositol 3-kinase J Biol Chem 1997 272 6136 6140 9045624
20. Malcolm KC Ross AH Qiu RG Symons M Exton JH Activation of rat liver phospholipase D by the small GTP-binding protein RhoA J Biol Chem 1994 269 25951 25954 7929302
21. Rumenapp U Geiszt M Wahn F Schmidt M Jakobs KH Evidence for ADP-ribosylation-factor-mediated activation of phospholipase D by m3 muscarinic acetylcholine receptor Eur J Biochem 1995 234 240 244 8529647
22. Schmidt M Rumenapp U Bienek C Keller J Eichel-Streiber C Jakobs KH Inhibition of receptor signaling to phospholipase D by Clostridium difficile toxin B. Role of Rho proteins J Biol Chem 1996 271 2422 2426 8576201
23. Shome K Vasudevan C Romero G ARF proteins mediate insulin-dependent activation of phospholipase D Curr Biol 1997 7 387 396 9197239
24. Shome K Nie Y Romero G ADP-ribosylation factor proteins mediate agonist-induced activation of phospholipase D J Biol Chem 1998 273 30836 30841 9804862
25. Aoe T Huber I Vasudevan C Watkins SC Romero G Cassel D Hsu VW The KDEL receptor regulates a GTPase-activating protein for ADP-ribosylation factor 1 by interacting with its non-catalytic domain J Biol Chem 1999 274 20545 20549 10400684
26. Nagel W Zeitlmann L Schilcher P Geiger C Kolanus J Kolanus W Phosphoinositide 3-OH kinase activates the beta2 integrin adhesion pathway and induces membrane recruitment of cytohesin-1 J Biol Chem 1998 273 14853 14861 9614087
27. Santy LC Frank SR Hatfield JC Casanova JE Regulation of ARNO nucleotide exchange by a PH domain electrostatic switch Curr Biol 1999 9 1173 1176 10531036
28. Kolanus W Nagel W Schiller B Zeitlmann L Godar S Stockinger H Seed B Alpha L beta 2 integrin/LFA-1 binding to ICAM-1 induced by cytohesin-1, a cytoplasmic regulatory molecule Cell 1996 86 233 242 8706128
29. Kliche S Nagel W Kremmer E Atzler C Ege A Knorr T Koszinowski U Kolanus W Haas J Signaling by human herpesvirus 8 kaposin A through direct membrane recruitment of cytohesin-1 Mol Cell 2001 7 833 843 11336706
30. Turner CE Brown MC Cell motility: ARNOand ARF6 at the cutting edge Curr Biol 2001 11 R875 R877 11696346
31. Ahn J Donner DB Rosen OM Interaction of the human insulin receptor tyrosine kinase from the baculovirus expression system with protein kinase C in a cell-free system J Biol Chem 1993 268 7571 7576 8463287
32. Emoto M Klarlund JK Waters SB Hu V Buxton JM Chawla A Czech MP A role for phospholipase D in GLUT4 glucose transporter translocation J Biol Chem 2000 275 7144 7151 10702282
33. Klarlund JK Holik J Chawla A Park JG Buxton J Czech MP Signaling complexes of the FERM domain-containing protein GRSP1 bound to ARF exchange factor GRP1 J Biol Chem 2001 276 40065 40070 11445584
34. Rizzo MA Shome K Watkins SC Romero G The recruitment of Raf-1 to membranes is mediated by direct interaction with phosphatidic acid and is independent of association with Ras J Biol Chem 2000 275 23911 23918 10801816
35. Langille SE Patki V Klarlund JK Buxton JM Holik JJ Chawla A Corvera S Czech MP ADP-ribosylation factor 6 as a target of guanine nucleotide exchange factor GRP1 J Biol Chem 1999 274 27099 27104 10480924
36. Cavenagh MM Whitney JA Carroll K Zhang C Boman AL Rosenwald AG Mellman I Intracellular distribution of Arf proteins in mammalian cells. Arf6 is uniquely localized to the plasma membrane J Biol Chem 1996 271 21767 21774 8702973
37. Rothman JE Wieland FT Protein sorting by transport vesicles Science 1996 272 227 234 8602507
38. Yang CZ Heimberg H D'Souza-Schorey C Mueckler MM Stahl PD Subcellular distribution and differential expression of endogenous AD P-ribosylation factor 6 in mammalian cells J Biol Chem 1998 273 4006 4011 9461590
39. Mansour M Lee SY Pohajdak B The N-terminal coiled coil domain of the cytohesin/ARNO family of guanine nucleotide exchange factors interacts with the scaffolding protein CASP J Biol Chem 2002 277 32302 32309 12052827
40. Nevrivy DJ Peterson VJ Avram D Ishmael JE Hansen SG Dowell P Hruby DE Interaction of GRASP, a protein encoded by a novel retinoic acid-induced gene, with members of the cytohesin family of guanine nucleotide exchange factors J Biol Chem 2000 275 16827 16836 10828067
41. Rizzo MA Shome K Vasudevan C Stolz DB Sung TC Frohman MA Watkins SC Romero G Phospholipase D and its product, phosphatidic acid, mediate agonist-dependent raf-1 translocation to the plasma membrane and the activation of the mitogen-activated protein kinase pathway J Biol Chem 1999 274 1131 1139 9873061
42. Klarlund JK Tsiaras W Holik JJ Chawla A Czech MP Distinct polyphosphoinositide binding selectivities for pleckstrin homology domains of GRP1-like proteins based on diglycine versus triglycine motifs J Biol Chem 2000 275 32816 32821 10913124
43. Frank SR Hatfield JC Casanova JE Remodeling of the actin cytoskeleton is coordinately regulated by protein kinase C and the ADP-ribosylation factor nucleotide exchange factor ARNO Mol Biol Cell 1998 9 3133 3146 9802902

PMID: 14551903
Accession ID: PMC212687
License: CC BY
Last Updated: 2021-01-05 08:21:03
Retracted: no
Citation: PLoS Biol. 2003 Oct 13; 1(1):e1
==== Front
PLoS BiolPLoS BiolpbioplosbiolPLoS Biology1544-91731545-7885Public Library of Science San Francisco, USA 10.1371/journal.pbio.0000001Research ArticleCell BiologyImmunologyMolecular Biology/Structural BiologyMus (Mouse)Homo (Human)A Functional Analysis of the Spacer of V(D)J Recombination Signal Sequences Functional Analysis of RSS SpacersLee Alfred Ian 
1
Fugmann Sebastian D 
1
Cowell Lindsay G 
2
Ptaszek Leon M 
3
Kelsoe Garnett 
2
Schatz David G david.schatz@yale.edu
1
1Howard Hughes Medical Institute, Section of Immunobiology, Yale University School of MedicineNew Haven, ConnecticutUnited States of America2Department of Immunology, Duke University Medical CenterDurham, North CarolinaUnited States of America3Ruttenberg Cancer Center, Mount Sinai School of Medicine of New York UniversityNew York, New YorkUnited States of America10 2003 13 10 2003 13 10 2003 1 1 e11 6 2003 10 7 2003 Copyright: © 2003 Lee et al.2003This is an open-access article distributed under the terms of the Creative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are properly credited.
V(D)J Recombination and the Evolution of the Adaptive Immune System 

Functional Analysis of RSS Spacers 
During lymphocyte development, V(D)J recombination assembles antigen receptor genes from component V, D, and J gene segments. These gene segments are flanked by a recombination signal sequence (RSS), which serves as the binding site for the recombination machinery. The murine Jβ2.6 gene segment is a recombinationally inactive pseudogene, but examination of its RSS reveals no obvious reason for its failure to recombine. Mutagenesis of the Jβ2.6 RSS demonstrates that the sequences of the heptamer, nonamer, and spacer are all important. Strikingly, changes solely in the spacer sequence can result in dramatic differences in the level of recombination. The subsequent analysis of a library of more than 4,000 spacer variants revealed that spacer residues of particular functional importance are correlated with their degree of conservation. Biochemical assays indicate distinct cooperation between the spacer and heptamer/nonamer along each step of the reaction pathway. The results suggest that the spacer serves not only to ensure the appropriate distance between the heptamer and nonamer but also regulates RSS activity by providing additional RAG:RSS interaction surfaces. We conclude that while RSSs are defined by a “digital” requirement for absolutely conserved nucleotides, the quality of RSS function is determined in an “analog” manner by numerous complex interactions between the RAG proteins and the less-well conserved nucleotides in the heptamer, the nonamer, and, importantly, the spacer. Those modulatory effects are accurately predicted by a new computational algorithm for “RSS information content.” The interplay between such binary and multiplicative modes of interactions provides a general model for analyzing protein–DNA interactions in various biological systems.

Spacers not only ensure that the distance between the nonamer and heptamer is correct but they also regulate recombination activity by providing protein-binding sites along the DNA sequences that affect recombination
==== Body
Introduction
During B- and T-lymphocyte development, the immunoglobulin (Ig) and T-cell receptor (TCR) genes are assembled from discrete V, D, and J gene elements via a process of genomic rearrangements known as V(D)J recombination (Fugmann et al. 2000a; Hesslein and Schatz 2001). V(D)J recombination occurs in two steps: a cleavage phase, in which DNA double-strand breaks are created, followed by a joining phase (Fugmann et al. 2000a). During cleavage, the lymphoid-specific recombinase proteins, RAG1 and RAG2, presumably together with the accessory DNA-binding factor HMG-1/2, bind recombination signal sequences (RSSs) located adjacent to each rearranging gene element. A complex consisting of RAG and HMG proteins bound to a single RSS is then thought to capture a second RSS (Jones and Gellert 2002; Mundy et al. 2002); within this synaptic complex, the RAG proteins introduce double-strand breaks at the junctions between each RSS and its associated gene element (Hiom and Gellert 1998). In the joining phase, ubiquitous DNA repair factors involved in nonhomologous end joining, in the presence of the RAG proteins, ligate the cleaved ends, generating two types of recombinant junctions: precise signal joints (SJs) and imprecise coding joints (CJs) (Bassing et al. 2002).

RSSs are an essential part of V(D)J recombination, as their presence is both necessary and sufficient to direct RAG-mediated recombination on artificial substrates. Sequence alignments of RSSs suggested that each signal can be dissected into three components: a conserved heptamer (consensus: 5′-CACAGTG) and a conserved nonamer (consensus: 5′-ACAAAAACC), separated by a poorly conserved spacer of either 12 ± 1 or 23 ± 1 bp (Tonegawa 1983; Akira et al. 1987; Ramsden et al. 1994). The heptamer is the site of DNA cleavage (Roth et al. 1992), while the nonamer provides a major binding surface for RAG1 (Difilippantonio et al. 1996; Spanopoulou et al. 1996; Nagawa et al. 1998; Swanson and Desiderio 1998). Spacer length restricts recombination according to the “12/23 rule”; efficient recombination occurs between two gene elements only when one element is flanked by an RSS with a 12 bp spacer (12-RSS) and the other by an RSS with a 23 bp spacer (23-RSS) (Tonegawa 1983).

Despite the enormous specificity that RSSs confer on the recombination process, the recombination signals themselves demonstrate a remarkable degree of sequence heterogeneity. Only the first three nucleotides of the heptamer and the fifth and sixth positions of the nonamer show almost perfect conservation (Ramsden et al. 1994) and are therefore thought to be the major determinants of RSS specificity and function. Mutations in any of these five “critical” nucleotides, alone or in combination, essentially abolish recombination (Tonegawa 1983; Akira et al. 1987; Hesse et al. 1989). The roles of the remaining “noncritical” heptamer and nonamer nucleotides are less understood. Some studies observed that mutations in these lesser-conserved residues have comparatively milder phenotypes unless present in combination (Tonegawa 1983; Hesse et al. 1989). Others, however, reported that nonconsensus deviations of noncritical residues lead to vastly different recombination efficiencies, resulting in significant differences in gene element usage in the unselected antigen receptor repertoire (Ramsden and Wu 1991; Suzuki and Shiku 1992; Connor et al. 1995; Larijani et al. 1999).

Our current knowledge about the functional role of the spacer is that its length is crucial in directing V(D)J recombination (Tonegawa 1983; Hesse et al. 1989). Comprehensive sequence alignments show that the spacer possesses some degree of sequence conservation, albeit at a level much lower than that of the heptamer or nonamer (Ramsden et al. 1994). This suggests that there is little or no selective pressure for spacers to adopt a given sequence. Studies examining the effects of different spacer sequences on recombination activity have yielded seemingly conflicting results. An early report found up to a 15-fold effect of different spacer sequences (Akira et al. 1987), while follow-up studies observed either no effect (Wei and Lieber 1993; Akamatsu and Oettinger 1998) or up to 6-fold effects (Fanning et al. 1996; Nadel et al. 1998; Larijani et al. 1999). This suggests that spacer sequence may affect recombination activity, but a comprehensive picture of the rules that govern how it does so is lacking.

One limitation inherent in many prior RSS studies is that they have often been performed in the context of RSSs with a preponderance of consensus nucleotides. While such analyses have been useful in characterizing the most conserved or critical determinants of RSS function, the contributions of other nucleotides are potentially masked in RSSs with high consensus nucleotide representation. That most endogenous RSSs do not contain consensus heptamer and/or nonamer motifs further suggests the need for a careful study of individual RSS nucleotides in the context of physiologically relevant RSSs.

We have performed an extensive analysis of the functional properties of RSS elements in the context of endogenous recombination signals. To explore the nature of the complex relationships that might exist among different elements and positions in the RSS, we started with the nonfunctional RSS associated with the murine Jβ2.6 pseudogene element of the TCRβ locus (Jβ2.6 RSS). While most such pseudogene elements are flanked by RSSs with crippling mutations (Akira et al. 1987), Jβ2.6 is unique in that the sequence of its flanking RSS suggests no obvious explanation for its complete lack of activity (Figure 1). All of the critical residues are conserved, and each nonconsensus nucleotide in the heptamer and nonamer is represented in at least one other functional RSS in the TCRβ locus (Figure 1). A systematic analysis of Jβ2.6/consensus hybrid RSSs revealed that the nonamer, by itself, is the biggest determinant of Jβ2.6 RSS activity and that the lack of Jβ2.6 RSS function is due to the concerted action of nonconsensus nucleotides throughout the entire RSS, including the spacer. Surprisingly, we found that in combination with other consensus elements, an artificial consensus spacer can markedly boost recombination activity, while an anticonsensus spacer strongly impairs activity. Furthermore, in a genetic screen for functional spacer sequences, we observe a selective pressure for substrates with an increased representation of consensus nucleotides. Our results provide strong support for the model that RSS activity is a summation of numerous complex interactions between the RAG proteins and the RSS, involving not only the heptamer and nonamer but also most (if not all) basepairs of the spacer.

Figure 1 Recombination Signal Sequences
Heptamer, spacer, and nonamer elements of 12-RSSs referred to in this study are shown. “Cons.” and “Anti-Cons.” denote the consensus and anticonsensus 12-RSSs, respectively. VκL8, Jβ2.6, and Jβ2.2 are murine 12-RSSs. “Jβ Cons.” denotes the consensus RSS compiled for all functional 12-RSSs in the murine Jβ1 and Jβ2 clusters. Where more than one nucleotide is listed at any given position, this indicates a shared preponderance of those nucleotides. For consensus RSSs, nucleotides in bold indicate almost absolute conservation; for the anticonsensus RSS, bold nucleotides are almost completely absent. Nucleotides in lowercase italics appear at slightly reduced frequencies compared to the other nucleotides listed. “Jβ-G/-A/-T/-C” and the corresponding numbers indicate the number of functional RSSs in the murine Jβ1/Jβ2 clusters at which the respective nucleotide appears at the designated position. At the top of the figure, the position of each nucleotide is labeled with respect to the first position of the respective element.

Results
In Vivo Assay for Recombination
We generated a series of recombination substrates to measure the ability of various hybrid Jβ2.6/consensus 12-RSSs to rearrange to a “standard” 23-RSS (consisting of consensus heptamer and nonamer elements flanking a spacer from the functional Ig Jκ1 RSS). This standard 23-RSS was used instead of the natural Jβ2.6 RSS partner (the 23-RSS flanking Dβ2), since the substrates containing the Dβ2 23-RSS showed much lower levels of recombination in our hands (data not shown). The 12-RSS coding flank was the same for all constructs, namely that of Jβ2.6. For our study, a polymerase chain reaction (PCR)-based assay (Figure 2, top) was employed, which allowed us to visualize recombination efficiencies across a >1,000-fold range. The recombination substrates were transfected into the human embryonic kidney cell line 293T along with constructs expressing full-length RAG1 and RAG2 proteins, and recombination frequencies were measured by PCR using primers that amplify SJs. To confirm that the amplified products in our PCR assay were bona fide SJs, we demonstrated that they could be cleaved efficiently with ApaLI restriction endonuclease, which cuts precise RSS–RSS junctions (data not shown). The amount of recombination substrate recovered from each transfection was measured by PCR and used to normalize the recombination activity. Although we assayed primarily for SJ formation, analyses of CJ formation yielded parallel results (data not shown). As a reference, we used a substrate containing the 12-RSS from the TCR Jβ2.2 gene element (see Figure 1), which recombines at low but detectable levels, as measured both in our system and during T-lymphocyte development (Figure 2, lanes 1–4) (Livàk et al. 2000).

Figure 2 Recombination Activities on Hybrid Jβ2.6/Consensus RSSs
A diagram of the recombination assay (SJ formation) is shown (top). Activities were measured on substrates containing the indicated hybrid 12-RSS and a standard 23-RSS. H, Sk, Sc, or N denotes the consensus heptamer, VκL8 spacer, consensus spacer, or consensus nonamer, respectively; each 12-RSS bears the indicated combination of consensus/VκL8 elements, with the remaining elements belonging to Jβ2.6 RSS. To determine relative recombination efficiencies, the amount of SJs was first corrected for DNA recovery, then normalized to the values obtained for the substrate containing the Jβ2.2 RSS. Relative recombination efficiencies for each of three experiments are shown as bar graphs; the average value is shown below each sample. The gels shown here correspond to Experiment 3 and represent products of PCRs on 10-fold dilutions of recovered plasmid DNA.

Consensus Heptamer, Spacer, and Nonamer Replacements
Recombination of Jβ2.6 RSS is below the level of detection of our assay (Figure 2). Substitution of a consensus heptamer (H) into the Jβ2.6 RSS elevates the recombination frequency to levels just above background (Figure 2, lanes 13–16). Similarly, substitution of a spacer from a standard, functional 12-RSS (recombination signal sequence spacer [Sk], from Ig VκL8; see Figure 1) or of an artificial consensus spacer (Sc) only marginally restores recombination (Figure 2, lanes 17–24). By contrast, substitution of a consensus nonamer (N) boosts recombination activity to the level of Jβ2.2 RSS (Figure 2; compare lanes 1–4 to 25–28), approximately 20-fold higher than substitution of H, Sk, or Sc alone and at least two orders of magnitude above Jβ2.6 RSS. Therefore, the nonamer, by itself, is the biggest single determinant of Jβ2.6 RSS activity. The combination of a consensus heptamer and nonamer (H–N) further increases activity approximately 10-fold above N alone (Figure 2, lanes 45–48). Hence, the cumulative effects of nonconsensus mutations in the heptamer and nonamer elements of Jβ2.6 RSS are quite large.

In combination with a consensus heptamer and/or a consensus nonamer, the presence of either the VκL8 or the consensus spacer markedly enhances recombination activities above those observed with the Jβ2.6 RSS spacer (Figure 2, lanes 29–44). Although there is some fluctuation between experiments, in each replicate the greatest enhancement by the Sk or Sc spacer is seen in combination with a consensus heptamer: on average, H–Sk and H–Sc are 30- to 50-fold higher than H alone. By comparison, Sk–N and Sc–N are 3- to 8-fold higher than N, while H–Sk–N and H–Sc–N are 3- to 9-fold higher than H–N. Thus, a functional spacer can, in most cases, “rescue” the effects of a nonconsensus nonamer more fully than the effects of a nonconsensus heptamer, suggesting that the spacer has greater functional overlap with the nonamer than with the heptamer.

Single-Nucleotide Consensus Replacements
The heptamer and nonamer of Jβ2.6 RSS differ from the consensus in only five positions (see Figure 1): the last three nucleotides of the heptamer and the second and fourth nucleotides of the nonamer. To determine which of these nucleotides make the greatest contributions to Jβ2.6 RSS activity, we introduced the respective consensus nucleotides individually at each of these positions. Since substitution of a consensus heptamer alone yields very low recombination levels (Figure 2), we assayed single-nucleotide heptamer replacements (H[5], H[6], and H[7]) in combination with a consensus spacer. We also assayed substrates containing H(5) combined with a consensus nonamer or with both consensus spacer and nonamer elements. All single-nucleotide heptamer replacements result in significant partial restoration of activity, to levels at least 50% of those obtained with the full consensus heptamer (data not shown). This suggests that the low activity of the Jβ2.6 RSS heptamer is due to contributions of all three nonconsensus nucleotides.

Substitution of a consensus nucleotide at either the second or fourth position of the nonamer (N[2] or N[4], respectively), alone or in combination with a consensus heptamer and/or spacer, partially reproduces the effects of the full consensus nonamer (Figure 3A). Interestingly, in each set of constructs, N(2) confers a greater restoration of activity than N(4): on average, constructs containing N(2) recombine at 50% the level of N, while constructs containing N(4) recombine at roughly 10% of N. This suggests that the recombination process has a greater preference for preserving a consensus C at the second position of the nonamer than a consensus A at the fourth position.

Figure 3 In Vivo Recombination Activities on Hybrid 12-RSSs with Nonamer Point Mutations or with the Anticonsensus Spacer
The plots, error bars, and values listed below each sample represent the averages of three experiments. Note that all recombination efficiencies presented in this figure were obtained from transfections/PCRs that were completely independent from those shown in Figure 2. Abbreviations are identical to those used in Figure 2.

(A) N(2) or N(4) denotes point substitution of the consensus nucleotide at the second or fourth position of the nonamer, respectively.

(B) Sac indicates substrates that contain an anticonsensus 12-RSS spacer.

Anticonsensus Spacer Replacements
In the presence of a consensus heptamer and/or nonamer, a consensus spacer markedly enhances recombination levels over the Jβ2.6 RSS spacer. We therefore wondered whether the presence of an artificial anticonsensus spacer (Sac) (see Figure 1), containing the least-conserved nucleotide at each position (Ramsden et al. 1994), would impair recombination. In all cases, Sac reduced recombination levels 10- to 20-fold compared to the already inefficient Jβ2.6 RSS spacer (Figure 3B; compare N to Sac–N, and H–N to H–Sac–N). In our experimental system, the consensus and anticonsensus spacer sequences are therefore capable of specifying a surprisingly large range of recombination efficiencies of up to two orders of magnitude.

Coupled Cleavage In Vitro
Two important questions arise from the results of these in vivo assays. First, do the differences in the RSS nucleotide sequences affect the cleavage or the joining phase of the reaction? Second, are the RAG proteins by themselves the only proteins that mediate the discrimination between various RSSs? To address these questions, we performed standard 12–23 coupled cleavage reactions using purified, truncated (core) RAG proteins (Figure 4A). The linear substrates for these reactions were amplified by PCR from the plasmids used in the transient recombination assay. The amount of coupled cleavage products from three independent sets of reactions was quantified (Figure 4C). While the consensus RSS (H–Sc–N) promotes efficient cleavage of up to 23% of the input substrate, the Jβ2.6 RSS is cleaved at extremely low levels, at or below the limit of detection (Figure 4A, lane 2). As expected from the in vivo experiments, Jβ2.2 is sufficient for low but clearly detectable cleavage (Figure 4A, lane 26). In agreement with the SJ formation data, the consensus nonamer substitution (N) boosts the level of cleavage significantly (Figure 4A, lane 6), while the introduction of Sk or Sc has less effect (Figure 4A, lanes 8 and 10). In contrast to our findings on SJ formation, the substrate containing a consensus heptamer (H) is as efficiently cleaved as that containing N (Figure 4A; compare lanes 4 and 6). Interestingly, all substrates containing a consensus nonamer (and to a lesser extent those harboring a consensus spacer) show a high level of single-site cleavage at the 12-RSS (Figure 4A, lanes 6, 10, 12, 18, and 20); such products, which are only rarely generated on extrachromosomal substrates in vivo (Steen et al. 1997), could account for a reduced level of coupled cleavage compared to the recombination efficiencies obtained for the respective constructs in our SJ assays. The underlying mechanism of this phenomenon is the topic of ongoing studies.

Figure 4 In Vitro Cleavage Reaction
(A and B) Coupled cleavage was performed using body-labeled DNA substrates containing a standard 23-RSS (filled triangle) and different 12-RSSs (open triangle) as indicated above the lanes. Reaction products were separated on 4% polyacrylamide gels. The identity of the bands is indicated by symbols located between the gels; an arrow indicates the double cleavage product, while an asterisk marks single-site cleavage products. The gels shown here correspond to Experiment 2.

(C and D) The intensity of the bands from three individual experiments (see legend) was quantified and the average cleavage efficiency calculated for each individual substrate (indicated below the chart). The efficiencies are displayed as relative to those obtained for Jβ2.2, which were arbitrarily set to 1.

Interestingly, a favorable spacer sequence (Sk or Sc), when paired with H or N, boosts cleavage over the Jβ2.6 RSS spacer (Figure 4A, lanes 12, 14, 16, and 18). The levels of cleavage for H–Sk or H–Sc are reproducibly higher than those for Sk–N or Sc–N; although the effect is less striking than for SJ formation, the limits of detection in the coupled cleavage assay dictate that this assay spans a much narrower range of activities than the SJ formation assay. To further address the role of spacer sequences in our coupled cleavage system, we performed another set of experiments using the substrates containing the anticonsensus spacer (Sac) (Figure 4B and 4D). In conjunction with either consensus heptamer (H–Sac) or consensus nonamer (Sac–N), the anticonsensus spacer reduces cleavage 5- to 10-fold compared to the consensus spacer (H–Sc or Sc–N) (Figure 4C and 4D) and 3-fold compared to the Jβ2.6 RSS spacer (H or N) (Figure 4B; compare lanes 4 and 8 to lanes 6 and 10, respectively). This suggests that the Jβ2.6 RSS spacer, although “poor” compared to Sk or Sc, is still more proficient for cleavage than Sac.

RSS Binding
It is likely that differences in the nucleotide sequences of the RSS lead to variations in the stability of RAG–RSS complexes (Hiom and Gellert 1997; Akamatsu and Oettinger 1998; Swanson and Desiderio 1998). This idea provides one obvious explanation for the observed differences in SJ formation and cleavage efficiency among the various analyzed 12-RSSs. To address this possibility, we analyzed binding of the RAG proteins to individual isolated 12-RSSs, since the 23-RSS remained identical in all experiments described above. Binding was assessed in standard gel-shift assays using oligonucleotide substrates containing the respective 12-RSSs (Figure 5A). All binding assays were performed three times; the quantitation of binding for each RSS relative to Jβ2.2 is displayed in Figure 5B. (Note that the amount of shifted complex has been normalized for the amount of free probe, which contributes to the fact that, between some samples, visual assessment of relative binding activities are less striking than quantitative measurements.) As expected, the consensus 12-RSS (H–Sc–N) shows the highest binding efficiency, while binding to the endogenous Jβ2.6 RSS is weak, about 2-fold reduced compared to our standard, the functional Jβ2.2 12-RSS. Given that, as with the coupled cleavage assay, the range of activities in the binding assay is much narrower than in the SJ formation assay, these results correlate well with those obtained in the other assays. Substitution of the individual consensus elements H, Sc, and N, however, led to surprising results. While the consensus nonamer (N) sequence, as expected, increases the level of binding (up to that of Jβ2.2), the consensus spacer (Sc) alone has no effect on binding at all, and the consensus heptamer (H) consistently reduces the level of binding. The consensus spacer boosts binding only in the context of a consensus nonamer (the ratios of Sc–N:N and H–Sc–N:H–N are greater than H–Sc:H), and the consensus heptamer contributes significantly to RAG–RSS interactions in this assay only when both spacer and nonamer are consensus sequences (H–Sc–N:Sc–N > H–N:N or H:Jβ2.6 RSS). This indicates that the nonamer is the predominant element determining the stability of the initial RAG–HMG–RSS complex while the heptamer makes additional important contributions to cleavage and recombination not reflected in this binding assay.

Figure 5 In Vitro Binding
(A) Binding assays were performed using the 5′-end-labeled 12-RSS substrates indicated above the lanes. Each reaction contained identical amounts of DNA substrate. Owing to differences in the end-labeling efficiencies, the quantitation (shown in [B]) is required to make quantitative comparisons. The gels shown here correspond to Experiment 3.

(B) The relative amount of substrate in the shifted complex was determined. The binding efficiencies from three independent experiments were calculated relative to the binding seen for Jβ2.2 oligonucleotides (which were arbitrarily set to 1). The average value is displayed below the chart.

In the context of a consensus nonamer, the consensus spacer reproducibly enhances binding more than a consensus heptamer (Sc–N > H–N). In contrast, the anticonsensus spacer (H–Sac–N) reduces binding about 3-fold compared to H–Sc–N (Figure 5A and 5B). The effects of Sc–N compared to Sac–N are also clearly visible. Interestingly, the levels of binding in the presence of Sac are very similar to those obtained for the respective RSSs containing the original Jβ2.6 RSS spacer, in contrast to the comparative effects of the two spacers on cleavage (see Figure 4).

Taken together, the results of our binding studies underline clearly that the reduced ability of the Jβ2.6 RSS to participate in the initial interaction with the RAG complex, and hence the subsequent steps of V(D)J recombination, is caused not solely by the Jβ2.6 RSS nonamer but also by the “inefficient” spacer sequence. This indicates that the spacer helps the nonamer to efficiently lock the RAG proteins onto the RSS. The heptamer can contribute to this only when interactions with the other two elements are favorable.

Genetic Screen for Functional Spacer Sequences
Although the RSS spacer is poorly conserved and no naturally occurring RSS has yet been identified that bears the published consensus spacer sequence, our results show that the presence of the most- or least-conserved nucleotides at all positions of the spacer dramatically alters recombination activities of RSSs that contain a consensus heptamer and/or nonamer. This suggests that a functional preference exists for certain spacer sequences over others. We therefore established a genetic screen for functional spacer sequences in which each position of the spacer was randomized to contain either a consensus or an anticonsensus nucleotide (Sc/Sac). Because the greatest effect of the consensus spacer in our experiments is seen in combination with a consensus heptamer (H–Sc), the randomized spacer was analyzed in the context of 12-RSSs containing a consensus heptamer and the Jβ2.6 RSS nonamer (H–Sc/Sac). The H–Sc/Sac library contained roughly 80,000 clones, sufficient to represent each of the 4,096 possible spacer sequences multiple times (data not shown).

We transfected the H–Sc/Sac library into 293T cells together with vectors expressing full-length RAG1 and RAG2, and we cloned and sequenced PCR-amplified SJs. As a control, we analyzed PCR products corresponding to unrearranged substrates from library pools transfected in the absence of RAG1 and RAG2 (Figure 6). This control pool shows a bias toward the presence of C nucleotides (the consensus nucleotide at positions 4 and 7–9 of the spacer, and the anticonsensus nucleotide at positions 1 and 6), such that the overall bias of the unselected library is slightly toward the consensus spacer (total consensus/total anticonsensus nucleotides = 1.19), consistent with sequence analysis of untransfected library clones (data not shown). Sequence analysis of amplified SJs reveals an overall enrichment for consensus spacer nucleotides over the unrearranged control (total consensus/total anticonsensus nucleotides = 1.73 for SJs, versus 1.19 for control). Spacer positions 1–5 (adjacent to the heptamer) and 8–11 all show a preference for the consensus nucleotide; the remaining positions show little or no preference for the consensus or in one case (position 7) even an enrichment for the anticonsensus nucleotide (Figure 6, white bars). The strongest preference for consensus is seen at position 5, which shows almost a 3-fold enrichment over the unrearranged control; interestingly, previous mutation analyses have implicated this spacer position as having a role in affecting recombination levels (Fanning et al. 1996; Larijani et al. 1999). In general, the degree of enrichment at any given position reflects the degree to which the consensus nucleotide is represented among the endogenous RSS repertoire (Figure 6) (Ramsden et al. 1994).

Figure 6 Genetic Screen for Preferred Spacer Sequences
A plasmid library containing 12-RSSs with a consensus heptamer and either consensus or anticonsensus nucleotides at each position of the spacer was screened for spacers with higher activity using either in vivo recombination or in vitro coupled cleavage assays (see text for details).  The number of library clones screened was >105. In total, 240 sequences from two independent in vivo experiments and 205 sequences from two in vitro screens were analyzed. The relative enrichment for a consensus over an anticonsensus nucleotide at each position was calculated (taking the bias in the starting library into account). The average from two experiments is displayed in the bar graph and the values are displayed above or below the bars. The log2 of the ratio of the frequency of consensus and anticonsensus nucleotides at each position is displayed; hence, a value of one indicates that the respective nucleotide occurs two times more frequently in the selected population than in the starting library. In addition, the degree of conservation of each nucleotide is indicated (Ramsden et al. 1994).

To determine whether the preferred spacer sequences for SJ formation and cleavage differ, the library screen was also performed in vitro. To obtain artificial SJs from our biochemical cleavage assays, T4 ligase was added to the deproteinized cleavage products, which circularized the cleavage product containing two signal ends. The sequence analysis of such artificial SJs from two independent cleavage reactions showed that positions 2–5 as well as positions 8–11 of the spacer are enriched for consensus over anticonsensus sequences (Figure 6, black bars). While these observations mirror the SJ formation data, the nucleotide located at position 1 (and to some extent position 3) seems less important for coupled cleavage than for recombination in vivo. Similar to the in vivo experiment, position 5 shows the highest magnitude of enrichment for the consensus (about 4-fold). The differences between the results of the two experimental systems (SJ formation in vivo and cleavage in vitro) could be a reflection of the number of sequences obtained in each type of analysis (200–250) or could represent differences in the nucleotide requirements of spacer participation in cleavage versus SJ formation. Overall, our experiments indicate that spacer effects are largely mediated by the RAG proteins and occur, at least in part, in the first phase of V(D)J recombination: the recognition of the RSSs, their synapsis, and the cleavage step.

Correlation with a Computational Model for RSS Function
The observation that an RSS spacer can act in concert with the noncritical residues of the heptamer and nonamer to drastically modulate RSS activity suggests the need for models of RSS function that take into account complex functional relationships among the different nucleotides. A predictive algorithm for quantitatively assessing the potential of a given DNA sequence to undergo V(D)J recombination has recently been developed (Cowell et al. 2002, 2003). This algorithm calculates the theoretical recombination potential, or RSS information content (RIC) score, by examining internucleotide relationships within a given DNA sequence.

We calculated RIC scores for the hybrid Jβ2.6/consensus RSSs used in this study, and we compared them to the experimental binding, cleavage, and recombination values (Figure 7A and 7B; data not shown). The correlation between RIC scores and our experimental data is striking. The RIC score for Jβ2.6 RSS is below the threshold (−40) for sequences that would be expected to recombine. The addition of consensus heptamer and/or nonamer elements boosts RIC scores, mirroring the increases in binding, cleavage, and SJ formation. Of particular interest is the fact that effects of consensus and anticonsensus spacers on binding/cleavage/recombination are prominently reflected in the RIC scores as well. Intriguingly, RIC scores appear to be more strongly correlated with cleavage (rS = 0.90) than with binding (rS = 0.86) and most correlated with SJ formation (rS = 0.96). The correlations between our experimental data and RIC scores suggest that the failure of Jβ2.6 RSS to recombine and the ability of consensus heptamer, spacer, and nonamer elements to rescue Jβ2.6 RSS activity are functions of how well RSS structure corresponds to that of a preferred sequence. In this case, the selective advantage of the consensus RSS is not limited to a few critical nucleotides in the heptamer or nonamer but, rather, extends throughout the length of the RSS, even in regions (e.g., the spacer) that were previously thought to be unimportant.

Figure 7 Theoretical Predictions of RSS Qualities
The average recombination/cleavage efficiencies obtained in the in vivo experiments (A) and in vitro assays (B) are plotted against the RIC scores for the 12-RSS in the respective recombination substrates. Note that the values obtained from the in vitro cleavage assays were normalized to account for differences in the detection range of individual experiments.

Further support for the potential of the RIC score as a theoretical measure for RSS activity arises from our genetic screen. For both the in vivo and the in vitro screens, the mean RIC score of the 12-RSSs in the enriched population is higher than that of the starting pool (data not shown), and those differences are statistically significant (Student's t test and the Mann–Whitney test, p<0.0002 for all tests). This indicates that the RIC score is able to predict the quality of RSSs and that this ability is not limited to the well-conserved heptamer and nonamer but also applies to the far more diverse spacer.

Discussion
RSSs are the DNA elements that direct and control the V(D)J recombination reaction. In the TCR loci, differences in the abilities of individual RSSs to recombine with each other are a significant determinant of variations in the frequencies with which gene elements appear in the mature TCR population (Livàk and Petrie 2002 and references therein). The molecular basis of such differences in intrinsic recombination activities lies in the remarkable sequence diversity of endogenous RSSs. Previous studies using consensus or nearly consensus RSSs suggested that only a handful of absolutely conserved nucleotides in the heptamer and nonamer serve as the major determinants of RSS specificity and function. These studies, however, did not take into account the fact that the vast majority of endogenous RSSs do not contain fully consensus elements; hence, the physiologic roles of lesser-conserved RSS nucleotides are likely of much greater significance than previously estimated.

Contributions of Individual Elements
Starting from the nonfunctional Jβ2.6 RSS, we asked the following question: what effects do a perfect heptamer, nonamer, or spacer and combinations thereof have in an inactive or poorly active RSS? We show that a number of mutations in noncritical RSS positions are required to convert Jβ2.6 RSS into a highly active 12-RSS or to convert a highly active RSS (H–Sk–N or H–Sc–N) into a completely nonfunctional, pseudogene-type RSS. Our experiments demonstrate that all RSS nucleotides, including the spacer element and the noncritical positions of the heptamer and nonamer, have some sequence-directive roles. In general, we observe that the magnitude of the effects of unfavorable nucleotides in noncritical RSS positions is dependent on the presence of other unfavorable nucleotides. This explains why, in previous studies using largely consensus RSSs, the effects of nonconsensus nucleotides at the noncritical positions were concluded to be less significant (Tonegawa 1983; Hesse et al. 1989).

Contributions of Individual Nucleotides in Jβ2.6 RSS
The Jβ2.6 RSS heptamer differs from the consensus in the fifth, sixth, and seventh positions; none of these is drastically more important than any other in specifying overall heptamer function (data not shown). The Jβ2.6 RSS nonamer differs from the consensus in the second and fourth positions (see Figure 1), and the G at the fourth position disrupts the poly(A) tract present in the consensus nonamer. Previous footprint analyses and studies on the homologous DNA-binding domain of the bacterial Hin recombinase (Feng et al. 1994) suggest that RAG1 may bind the nonamer in the minor groove of this poly(A) tract (Spanopoulou et al. 1996; Akamatsu and Oettinger 1998; Nagawa et al. 1998). Hence, we expected that restoration of the poly(A) tract of the nonamer would have a greater boosting effect on recombination levels than a consensus substitution at the second position. Instead, the opposite is true, regardless of the sequences in the remainder of the RSS (see Figure 3). Having the consensus cytidine at position 2 creates a CA step within the nonamer. Such CA steps have been implicated in alternative DNA structures (Gorin et al. 1995); while previous discussion has focused on the CA steps present at the site of cleavage in the heptamer, it is possible that a single CA step in the nonamer is important for the RAG complex to identify the subsequent downstream poly(A) tract.

Defects in RAG Binding to Jβ2.6 RSS
Previous binding studies have shown that the nonamer is the key element for initial RAG–RSS interactions and that mutations within the nonamer can strongly reduce or even completely abolish formation of the 12-SC (signal complex) (Hiom and Gellert 1997; Akamatsu and Oettinger 1998). In contrast, mutating the entire heptamer leads only to a partial decrease in 12-SC formation, and, importantly, the absolutely conserved “CAC” triplet contributes only as much to binding as the last four nucleotides of the heptamer (Akamatsu and Oettinger 1998). Our gel-shift studies recapitulate these observations with the Jβ2.6 RSS heptamer and nonamer (see Figure 5). Moreover, a hybrid Jβ2.6/consensus RSS containing a consensus nonamer can promote 12-SC formation as efficiently as the functional Jβ2.2 RSS (see Figure 5). This explains why replacement of the Jβ2.6 RSS nonamer with a consensus nonamer can restore recombination to low but physiologically relevant levels (see Figure 2).

The effect of a consensus spacer on 12-SC formation exhibits striking plasticity (see Figures 2–5). Additionally, in our in vitro screen, the areas of the 12-RSS spacer most highly enriched for consensus nucleotides (see Figure 6) correlate with sites of spacer contacts identified in previous footprinting studies (spacer positions 2–5 and 9–11) (Akamatsu and Oettinger 1998; Nagawa et al. 1998; Swanson and Desiderio 1998; Swanson 2002). Given that the nonamer provides the most important contact surfaces, if strong interactions with the nonamer can form, then the presence of a consensus spacer may allow additional favorable contacts to be established, not only in the spacer itself, but even farther away, in the heptamer. By contrast, an unfavorable spacer (e.g., the Jβ2.6 RSS spacer or Sac) may structurally “insulate” protein–DNA contacts seen in the nonamer, such that potential heptamer contact surfaces that could otherwise contribute to overall 12-SC stability remain hidden. This may explain why a consensus heptamer, in the absence of a good nonamer, is unable to promote formation of a stable 12-SC complex.

Our in vitro cleavage assay integrates the effects of RSS binding, pairing, and actual DNA cleavage. Hence, the differences between the results of binding and cleavage assays suggest that the steps following initial binding (paired complex [PC] formation and DNA cleavage) are also regulated by spacer sequences. PC formation requires the recognition of the partner RSS with respect to its spacer length, and thus it is plausible that the sequence of spacers influences the protein–DNA contacts required for this compatibility test. Since it is within the PC that coordinated, synchronous DNA cleavage takes place (Hiom and Gellert 1998; West and Lieber 1998), it is conceivable that RSSs “communicate” with each other and that their spacer sequences therefore may affect the alignment of the cleavage site with respect to the recombinase active site. Such structural changes may underlie the phenomenon of the “beyond 12/23 rule” that restricts V(D)J recombination of the TCRβ locus, preventing recombination of certain 12–23 RSS pairs and favoring recombination of others (Jung et al. 2003). The 23 bp spacer of the Vβ RSSs is the critical element in dictating the strong preference of Vβ RSSs for the 12-RSS flanking the D segments as compared to the 12-RSS flanking the J segments, and this preference is regulated before or at the cleavage step (Jung et al. 2003). These intriguing findings, however, did not provide experimental insight into how a DNA motif whose sequence had previously been deemed unimportant could paradoxically play such an important role. Our findings provide a framework with which to understand how such an unexpected phenomenon might occur.

Finally, the differences between the in vitro cleavage and in vivo recombination assays indicate an additional role of the spacer sequence in the joining phase of the reaction. This seems plausible, since joining is thought to start with the controlled disassembly of the postcleavage complex in which the four DNA ends, including the RSSs, are held in intimate contact with each other, presumably by the RAG proteins (Hiom and Gellert 1998; Tsai et al. 2002). Spacer sequences might thus be involved in controlling the structure and stability of such complexes.

Relationship between Spacer Sequence Conservation and Recombination Activity
Based on comprehensive sequence alignments showing a small but significant degree of spacer sequence conservation (Ramsden et al. 1994), a few studies demonstrated reproducible effects of up to 6-fold of naturally occurring spacers on recombination levels (Fanning et al. 1996; Nadel et al. 1998). In transient transfection assays, we infer a much wider range of recombination efficiencies solely due to differences in spacer sequence. Strikingly, we observe that spacer sequence variably affects RSS activity depending on the extent to which each nucleotide of the spacer matches either the most- or the least-conserved nucleotide. This observation resolves some of the apparent discrepancies observed among previously published studies. For example, a poly(G) spacer, which reduces recombination 15-fold compared to a highly active control (Akira et al. 1987), contains one consensus and five anticonsensus residues; by contrast, a spacer containing intermixed G and C residues, which has no effect on recombination activity (Wei and Lieber 1993), contains five consensus and four anticonsensus residues.

A Structural Basis for the Ability of RAG Proteins to Recombine Highly Diverse RSSs
We find that progressive accumulation of nonconsensus nucleotides within an RSS progressively impairs recombination activity and that, at the less-conserved positions of an RSS, a multitude of nonconsensus nucleotides acting in concert can render the RSS completely inactive. This suggests that the RAG–RSS complex can tolerate or correct for a considerable amount of sequence and/or structural diversity. UV–cross-linking studies previously demonstrated RAG1 and RAG2 cross-linking to the heptamer, particularly near the site of cleavage (Eastman et al. 1999; Mo et al. 1999; Swanson and Desiderio 1999). Footprint analyses of the 12-SC show that complex formation is at least partly blocked by base or phosphate group modification on the spacer side of the heptamer, on both the heptamer- and nonamer-proximal sides of the spacer, and throughout the nonamer (Akamatsu and Oettinger 1998; Nagawa et al. 1998; Swanson and Desiderio 1998; Swanson 2002). The identified contact sites in the spacer coincide with the areas of the spacer that were preferentially found to be consensus type in our genetic screen (see Figure 6). Moreover, the observed recombination efficiencies of our hybrid substrates correlate well with the predicted recombination efficiencies from RIC analyses (see Figure 7A and 7B). Together, these findings support a unifying model in which the RAG proteins establish multiple contacts throughout the length of an RSS (including the spacer) that allow for fine-tuning of activity. Such an extensive network of RAG–RSS contacts within the recombinase complex would create a “structural buffer,” in which unfavorable nucleotides at only a few noncritical positions might be compensated for by favorable protein–DNA interactions at other positions. Conceptually similar models exist for the I-PpoI and I-CreI homing endonucleases, which cleave at recognition sites approximately 20 bp in length (Argast et al. 1998; Jurica et al. 1998), and which can tolerate sequence heterogeneity in cleavage sites. Both I-PpoI and I-CreI form direct sidechain interactions with most of the nucleotides in their recognition sites, and it is believed that the extensive protein–DNA contacts contribute to tolerance of sequence diversity.

Based on our in vivo, in vitro, and in silico analyses, we propose that the RAG–RSS complex contains two distinct types of protein–DNA interactions: “digital” (or binary) interactions of a strictly sequence-specific nature, and “analog” (or multiplicative) contacts that fine-tune the strength of the digital contacts (Travers 1993). Digital interactions are established with those nucleotides for which proper sequence is absolutely critical for activity (e.g., the first three nucleotides of the heptamer and positions 5 and 6 of the nonamer). Analog interactions describe local structural variations brought about by different sequences along the rest of the RSS. Disruption of digital interactions completely precludes complex formation (e.g., a single mutation of a critical residue in the consensus RSS can render it entirely inactive), yet digital interactions alone are not sufficient to establish complex formation (e.g., the critical residues by themselves cannot confer activity to the Jβ2.6 RSS).

This duality in the nature of protein–DNA contacts present within the RAG–RSS recombinase may be applicable to other biological systems, including other transposases, transcription factors, and DNA-binding proteins. In most protein–DNA interaction systems, the target sequence to which a protein binds contains some nucleotides that are absolutely critical, and others that are noncritical. Digital interactions are established with the absolutely conserved nucleotides in the form of sequence-specific binding, conferring a binary specificity; the digital contacts therefore determine whether a protein will bind (+1) or not (0). Analog contacts are then established with the lesser-conserved nucleotides; the analog interactions act as functional multipliers that determine the efficiency of complex stability, yielding a spectrum of binding efficiencies ranging from full activity (1 × Amax, where A = effect on binding efficiency due to analog interactions) to no activity (0 × Amin). Hence, the noncritical residues are crucial for determining how well a protein complex can exert its biological function.

By including so many nucleotides as requirements for RSS function, the V(D)J recombination system may have evolved to avoid random cleavage of DNA and translocation errors. If only the critical heptamer and nonamer nucleotides were required for activity, the frequency of cleavage at inappropriate or “cryptic” sites in the genome would be expected to be quite high. By contrast, the required participation of noncritical nucleotides in complex stability safeguards the reaction against uncontrolled cleavage. Hence, from the standpoint of controlled diversification of reaction specificity, it is beneficial for the recombinase to have evolved a spacer with a high degree of sequence heterogeneity, while maintaining intimate contact with the spacer nucleotides via analog interactions. The complex multiplier effect of analog contacts throughout the length of the RSS, superimposed onto specific digital contacts in the heptamer and nonamer, therefore confers upon the recombinase the critical ability to distinguish between inappropriate sites that happen to contain the requisite absolutely conserved nucleotides (e.g., the Jβ2.6 RSS) versus true binding sites whose sequences diverge markedly from the consensus (e.g., most endogenous RSSs).

Theoretical Predictions of RSS Quality
RIC scores provide a powerful tool for the prediction of RSS quality based on nucleotide sequence. This method generates statistical predictions of RSS function based on the physiologic 12- and 23-RSSs in the mouse antigen receptor gene loci. In our study, RIC scores accurately predicted the relative efficiencies with which RSSs were bound, cleaved, and rearranged (see Figure 7; data not shown). Interestingly, the capacity of RIC models to predict RSS quality is not restricted to sequence variability in the conserved RSS heptamer and nonamer; RIC scores also predict the effects of the RSS spacer sequence on RSS function with considerable accuracy.

It is striking that RIC scores correlate so well with SJ formation, less well with cleavage, and less well still with RSS binding. This supports the idea that individual nucleotides (and groups thereof) make distinct contributions to the different steps of the V(D)J recombination reaction. This concept is consistent with previous findings showing that the nonamer is a major determinant of binding while the influence of the heptamer becomes most apparent at the level of cleavage. Hence, the efficiency with which an RSS recombines represents an integration of its protein–DNA interactions throughout all steps of the reaction, and RIC scores provide a remarkably accurate prediction of this.

RIC models should be useful not only in guiding RSS mutation studies, but also in identifying potential cryptic RSSs in the genome, whose usage could lead to genomic alterations as an initial event leading to chromosomal translocations and cancer (Cowell et al. 2002, 2003). Furthermore, an identical mathematical approach could be useful for predicting binding sites for DNA-binding complexes (e.g., transcription factors) in general, since the algorithm incorporates the combination of both the digital and the analog DNA–protein interactions that determine the biological function of a given protein complex on a potential DNA target.

Materials and Methods

Oligonucleotides and plasmids.
The sequence of oligonucleotides used for cloning of recombination substrates and libraries are presented in Table S1. The oligonucleotides used in the gel-shift experiments are listed in Table S2, and the sequences of oligonucleotides used for PCR (INNE1, CIT4A, TL1, TL2, TL3, TL4, TL5, and TL6) have been described previously (Eastman et al. 1996; Leu et al. 1997).

The pSJΔ series of substrates for the in vivo recombination and in vitro cleavage assays was created as follows: pSF299 (Fugmann and Schatz 2001) was modified to create p299-Jβ2.6 by replacing the original 12-RSS with a Jβ2.6 12-RSS such that the 12/23-RSS pair is in deletional orientation; for all other substrates, the 12-RSS of p299-Jβ2.6, flanked by HindIII and SalI sites, was replaced with the respective annealed oligonucleotides (see Table S1).

To generate the library for the genetic screen, the oligonucleotide HSCSAC1 was synthesized that contained a 1:1 molar ratio of consensus:anticonsensus nucleotides at each position of the spacer and an additional randomized trinucleotide sequence downstream of the nonamer. The oligonucleotide SJLIBREV was annealed, the overhang was filled in using Klenow fragment (New England Biolabs, Beverly, Massachusetts), and the double-stranded fragment was digested with HindIII and SalI and ligated into the linearized p299-Jβ2.6 vector. Ligation reactions were transformed into DH5α, colonies were harvested into 120 ml of Luria broth (containing 100 μg/ml ampicillin), and plasmid DNA was prepared after an additional incubation at 37°C at 250 rpm for 15 min.

pEBB, pEBB-RAG1, and pEBB-RAG2 expression constructs have been described elsewhere (Roman et al. 1997).

Recombination assays.
Human embryonic kidney 293T cells were transfected with 6 μg of recombination substrate and 3 μg each of pEBB-RAG1 and pEBB-RAG2 using calcium phosphate as described previously (Fugmann and Schatz 2001); for control samples without RAG expression constructs, 6 μg of pEBB was substituted. After 48 h, DNA was recovered by rapid alkaline lysis preparation (RAP) (Hesse et al. 1987). PCR was performed on 10-fold serial dilutions in 20 μl reaction volumes containing 1× Taq buffer (Invitrogen, Carlsbad, California), 2 mM MgCl2, 0.1 mM each dNTP, 0.5 μM each oligo, and 0.2 U Taq (Invitrogen). To quantify DNA recovery, the oligonucleotide pair TL5/TL6 was used for the PCR (94°C for 15 s, 60°C for 15 s, 72°C for 30 s, for 18 cycles). To detect SJs, DNA samples were treated with DpnI, MluI, and XhoI to remove unreplicated and unrecombined plasmids. Oligonucleotides INNE1 and CIT4A were used to amplify SJs (94°C for 15 s, 60°C for 15 s, 72°C for 30 s, for 28 cycles). To detect CJs, RAP samples were treated with DpnI and CJs were amplified using primers TL2 and TL3. All PCR products were electrophoresed on native 4.5% polyacrylamide gels, stained with SYBR green, visualized using a Fluoroimager 595 (Molecular Dynamics, Sunnyvale, California), and quantified using ImageQuant software (Molecular Dynamics).

Genetic screen for functional spacer sequences.
293T cells were transfected with the plasmid library and RAG or pEBB constructs as described in the Results. Extrachromosomal DNA was extracted and samples were digested with either DpnI/MluI/XhoI (for cloning of SJs) or DpnI only (for cloning of unrearranged bands in no-RAG controls). PCR was performed using INNE1 and CIT4A primers, and samples were electrophoresed and stained as indicated above. The products corresponding to the appropriate SJ or unrearranged bands were excised, purified, and cloned into pCR2.1 using a TOPO-T/A cloning kit (Invitrogen). DNA was prepared from individual transformed colonies and sequenced.

The in vitro screen was performed using the plasmid library as the substrate in a standard coupled cleavage reaction. After proteinase K digestion, the products were precipitated and dissolved in 100 μl of 1× ligase buffer. T4 DNA ligase (1 μl) (New England Biolabs) was added and the mixture incubated at 16 °C for 4 h to create artificial SJs. The resulting plasmids were treated identically to the plasmids recovered after transfection in the in vivo screen.

Protein expression.
Recombinant GST-RAG2, MBP-RAG1, and HMG2 were expressed and purified as described previously (Spanopoulou et al. 1996; Eastman et al. 1999; Rodgers et al. 1999).

DNA-binding and cleavage assays.
The body-labeled DNA substrates for the cleavage assay were generated by PCR using the oligonucleotides TL1, TL4, and the respective recombination substrate as a template. The 12-RSS oligonucleotide substrates used in EMSA were generated by annealing the 5′-end-labeled top strand with an equimolar amount of the unlabeled respective bottom strand (see Table S2). Binding and cleavage reactions were performed as reported previously (Fugmann et al. 2000b), and gels were quantified using a Storm 820 PhosphorImager and ImageQuant software (Molecular Dynamics).

RIC score calculation and other computational analysis.
Statistical models of RSS correlation structure have been previously reported (Cowell et al. 2002) (Data S1).

Supporting Information
Data S1 RIC Score Calculation and Other Computational Analysis
(23 KB DOC).

Click here for additional data file.

 Table S1 Oligonucleotides for Cloning of Recombination Substrates
(31 KB DOC).

Click here for additional data file.

 Table S2 Oligonucleotides for Gel Shift Experiments
(23 KB DOC).

Click here for additional data file.

 We would like to thank N. H. Ruddle, N. D. Grindley, C. M. Radding, and all Schatz lab members for helpful discussions and suggestions. We also thank the W. M. Keck Foundation Biotechnology Resource Laboratory at Yale University for oligonucleotide synthesis and DNA sequencing. AIL was supported by a predoctoral fellowship from the Howard Hughes Medical Institute (HHMI). SDF is a postdoctoral fellow of the Irvington Institute for Immunological Research, and DGS is an Investigator of the HHMI. LGC received a Bioinformatics and Genome Technology Postdoctoral Fellowship from Duke University and is supported by a National Institutes of Health (NIH) Basic Immunology Training Grant (T32 AI52077-01) to Duke University Medical Center. This research was supported by grant RO1 AI-32524 to DGS and in part by grants AI-24335 and AI-49326 to GK from the NIH.


Conflicts of Interest. The authors have declared that no conflicts of interest exist.


Author Contributions. AIL, SDF, LGC, LMP, and DGS conceived and designed the experiments. AIL, SDF, and LGC performed the experiments. AIL, SDF, LGC, GK, and DGS analyzed the data. AIL, SDF, LGC, and LMP contributed reagents/materials/analysis tools. AIL, SDF, LGC, and DGS wrote the paper.

Academic Editor: Shizuo Akira, Osaka University.

Abbreviations
CJcoding joint

Hheptamer

Igimmunoglobulin

Nnonamer

PCpaired complex

PCRpolymerase chain reaction

RAPrapid alkaline lysis preparation

RICrecombination signal sequence information content

RSSrecombination signal sequence

Sacrecombination signal sequence spacer

Screcombination signal sequence spacer

SCsignal complex

SJsignal joint

Skrecombination signal sequence spacer from the VκL8 segment

TCRT-cell receptor.
==== Refs
References
Akamatsu Y  Oettinger MA   Distinct roles of RAG1 and RAG2 in binding the V(D)J recombination signal sequences Mol Cell Biol 1998 18 4670 4678 9671477 
Akira S  Okazaki K  Sakano H   Two pairs of recombination signals are sufficient to cause immunoglobulin V-(D)-J joining Science 1987 238 1134 1138 3120312 
Argast GM  Stephens KM  Emond MJ  Monnat RJ   I-Ppo I and I-Cre I homing site sequence degeneracy determined by random mutagenesis and sequential in vitro enrichment J Mol Biol 1998 280 345 353 9665841 
Bassing CH  Swat W  Alt FW   The mechanism and regulation of chromosomal V(D)J recombination Cell 2002 109 S45 S55 11983152 
Connor AM  Fanning LJ  Celler JW  Hicks LK  Ramsden DA    Mouse V(H)7183 recombination signal sequences mediate recombination more frequently than those of VHJ558 J Immunol 1995 155 5268 5272 7594539 
Cowell LG  Davila M  Kepler TB  Kelsoe G   Identification and utilization of arbitrary correlations in models of recombination signal sequences Genome Biol 2002 3 research0072.1 research0072.20 12537561 
Cowell LG  Davila M  Yang K  Kepler TB  Kelsoe G   Prospective estimation of recombination signal efficiency and identification of functional cryptic signals in the genome by statistical modeling J Exp Med 2003 197 207 220 12538660 
Difilippantonio MJ  McMahan CJ  Eastman QM  Spanopoulou E  Schatz DG   RAG1 mediates signal sequence recognition and recruitment of RAG2 in V(D)J recombination Cell 1996 87 253 262 8861909 
Eastman QM  Leu TMJ  Schatz DG   Initiation of V(D)J recombination in vitro  obeying the 12/23 rule Nature 1996 380 85 88 8598914 
Eastman QM  Villey IJ  Schatz DG   Detection of RAG protein–V(D)J recombination signal interactions near the site of DNA cleavage by UV cross-linking Mol Cell Biol 1999 19 3788 3797 10207102 
Fanning L  Connor A  Baetz K  Ramsden D  Wu GE   Mouse RSS spacer sequences affect the rate of V(D)J recombination Immunogenetics 1996 44 146 150 8662078 
Feng J-A  Johnson RC  Dickerson RE   
Hin  recombinase bound to DNA: The origin of specificity in major and minor groove interactions Science 1994 263 348 355 8278807 
Fugmann SD  Schatz DG   Identification of basic residues in RAG2 critical for DNA binding by the RAG1–RAG2 complex Mol Cell 2001 8 899 910 11684024 
Fugmann SD  Lee AI  Shockett PE  Villey IJ  Schatz DG   The RAG proteins and V(D)J recombination: Complexes, ends, and transposition Annu Rev Immunol 2000a 18 495 527 10837067 
Fugmann SD  Villey IJ  Ptaszek LM  Schatz DG   Identification of two catalytic residues in RAG1 that define a single active site within the RAG1/RAG2 protein complex Mol Cell 2000b 5 97 107 10678172 
Gorin AA  Zhurkin VB  Olson WK   B-DNA twisting correlates with base-pair morphology J Mol Biol 1995 247 34 48 7897660 
Hesse JE  Lieber MR  Gellert M  Mizuuchi K   Extrachromosomal DNA substrates in preB cells undergo inversion or deletion at immunoglobulin V-(D)-J joining signals Cell 1987 49 775 783 3495343 
Hesse JE  Lieber MR  Mizuuchi K  Gellert M   V(D)J recombination: A functional definition of the joining signals Genes Dev 1989 3 1053 1061 2777075 
Hesslein DG  Schatz DG   Factors and forces controlling V(D)J recombination Adv Immunol 2001 78 169 232 11432204 
Hiom K  Gellert M   A stable RAG1–RAG2–DNA complex that is active in V(D)J cleavage Cell 1997 88 65 72 9019407 
Hiom K  Gellert M   Assembly of a 12/23 paired signal complex: A critical control point in V(D)J recombination Mol Cell 1998 1 1011 1019 9651584 
Jones JM  Gellert M   Ordered assembly of the V(D)J synaptic complex ensures accurate recombination EMBO J 2002 21 4162 4171 12145216 
Jung D  Bassing CH  Fugmann SD  Cheng HL  Schatz DG    Extrachromosomal recombination substrates recapitulate beyond 12/23 restricted VDJ recombination in nonlymphoid cells Immunity 2003 18 65 74 12530976 
Jurica MS  Monnat RJ  Stoddard BL   DNA recognition and cleavage by the LAGLIDADG homing endonuclease I-Cre I Mol Cell 1998 2 469 476 9809068 
Larijani M  Yu CCK  Golub R  Lam QLK  Wu GE   The role of components of recombination signal sequences in immunoglobulin gene segment usage: A V81x model Nucleic Acids Res 1999 27 2304 2309 10325418 
Leu TMJ  Eastman QM  Schatz DG   Coding joint formation in a cell free V(D)J recombination system Immunity 1997 7 303 314 9285414 
Livàk F  Petrie H   Access roads for RAG-ged terrains: Control of T cell receptor gene rearrangement at multiple levels Semin Immunol 2002 14 297 309 12220931 
Livàk F  Burtrum DB  Rowen L  Schatz DG  Petrie HT   Genetic modulation of T cell receptor gene segment usage during somatic recombination J Exp Med 2000 192 1191 1196 11034609 
Mo X  Bailin T  Sadofsky MJ   RAG1 and RAG2 cooperate in specific binding to the recombination signal sequence in vitro 
 J Biol Chem 1999 274 7025 7031 10066757 
Mundy CL  Patenge N  Matthews AGW  Oettinger MA   Assembly of the RAG1/RAG2 synaptic complex Mol Cell Biol 2002 22 69 77 11739723 
Nadel B  Tang A  Escuro G  Lugo G  Feeney AJ   Sequence of the spacer in the recombination signal sequence affects V(D)J rearrangement frequency and correlates with nonrandom V-kappa usage in vivo 
 J Exp Med 1998 187 1495 1503 9565641 
Nagawa F  Ishiguro K  Tsuboi A  Yoshida T  Ishikawa A    Footprint analysis of the RAG protein recombination signal sequence complex for V(D)J type recombination Mol Cell Biol 1998 18 655 663 9418911 
Ramsden DA  Wu GE   Mouse κ light-chain recombination signal sequences mediate recombination more frequently than do those of λ light chain Proc Natl Acad Sci U S A 1991 88 10721 10725 1961738 
Ramsden DA  Baetz K  Wu GE   Conservation of sequence in recombination signal sequence spacers Nucleic Acids Res 1994 22 1785 1796 8208601 
Rodgers KK  Villey IJ  Ptaszek L  Corbett E  Schatz DG    A dimer of the lymphoid protein RAG1 recognizes the recombination signal sequence and the complex stably incorporates the high mobility group protein HMG2 Nucleic Acids Res 1999 27 2938 2946 10390537 
Roman CAJ  Cherry SR  Baltimore D   Complementation of V(D)J recombination deficiency in RAG-1(−/−) B cells reveals a requirement for novel elements in the N-terminus of RAG-1 Immunity 1997 7 13 24 9252116 
Roth DB  Nakajima PB  Menetski JP  Bosma MJ  Gellert M   V(D)J recombination in mouse thymocytes: Double-stranded breaks near T-cell receptor delta rearrangement signals Cell 1992 69 41 53 1313336 
Spanopoulou E  Zaitseva F  Wang F-H  Santagata S  Baltimore D    The homeodomain of Rag-1 reveals the parallel mechanisms of bacterial and V(D)J recombination Cell 1996 87 263 276 8861910 
Steen SB  Gomelsky L  Speidel SL  Roth DB   Initiation of V(D)J recombination in vivo: Role of recombination signal sequences in formation of single and paired double-strand breaks EMBO J 1997 16 2656 2664 9184212 
Suzuki H  Shiku H   Preferential usage of JH2  in D-J joinings with DQ52  is determined by the primary DNA sequence and is largely dependent on recombination signal sequences Eur J Immunol 1992 22 2225 2230 1516615 
Swanson PC   Fine structure and activity of discrete RAG–HMG complexes on V(D)J recombination signals Mol Cell Biol 2002 22 1340 1351 11839801 
Swanson PC  Desiderio S   V(D)J recombination signal recognition-distinct, overlapping DNA-protein contacts in complexes containing RAG1 with and without RAG2 Immunity 1998 9 115 125 9697841 
Swanson PC  Desiderio S   RAG-2 promotes heptamer occupancy by RAG-1 in the assembly of a V(D)J initiation complex Mol Cell Biol 1999 19 3674 3683 10207091 
Tonegawa S   Somatic generation of antibody diversity Nature 1983 302 575 581 6300689 
Travers A   DNA–protein interactions 1993 London Chapman and Hall 180 
Tsai CL  Drejer AH  Schatz DG   Evidence of a critical architectural function for the RAG proteins in end processing, protection, and joining in V(D)J recombination Genes Dev 2002 16 1934 1949 12154124 
Wei Z  Lieber MR   Lymphoid V(D)J recombination: Functional analysis of the spacer sequence within the recombination signal J Biol Chem 1993 268 3180 3183 8428995 
West RB  Lieber MR   The RAG–HMG1 complex enforces the 12/23 rule of V(D)J recombination specifically at the double-hairpin formation step Mol Cell Biol 1998 18 6408 6415 9774656

PMID: 0
Accession ID: PMC212688
License: CC BY
Last Updated: 2021-01-05 08:21:04
Retracted: no
Citation: PLoS Biol. 2003 Oct 13; 1(1):e4
==== Front
PLoS BiolPLoS BiolpbioplosbiolPLoS Biology1544-91731545-7885Public Library of Science San Francisco, USA 10.1371/journal.pbio.0000004SynopsisCell BiologyImmunologyMolecular Biology/Structural BiologyMus (Mouse)Homo (Human)Functional Analysis of RSS Spacers Synopsis10 2003 13 10 2003 13 10 2003 1 1 e4Copyright: © 2003 Public Library of Science.2003This is an open-access article distributed under the terms of the Creative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are properly credited.
V(D)J Recombination and the Evolution of the Adaptive Immune System 

A Functional Analysis of the Spacer of V(D)J Recombination Signal Sequences
==== Body
Based on sheer numbers, microbes should rule the world. Most don't cause disease, but those that do have the advantage of multiplying and mutating at a much faster rate than any multicellular organism can. So how does a slowly reproducing, trillion-celled organism like a human protect itself? By having the right weapon for the job—and that requires an incredibly diverse arsenal. A new study by a team of researchers from Yale University School of Medicine, Duke University Medical Center, and Mount Sinai School of Medicine demonstrates how the creation of that arsenal depends on a complex series of interactions between key genetic elements and proteins during the formation of the white blood cells called lymphocytes.

Two heavy hitters of the immune system—B and T cells—each produce unique protein receptors that specifically recognize and mediate the killing of the variety of potential foreign invaders, or antigens, such as bacteria, viruses, and parasites. (B cells make immunoglobulin, or antibodies, and T cells make T-cell receptors.) But these lymphocytes are unlike other cells: instead of making proteins from genes they inherited, they custom-make their genes by recombining fragments of their genes into new configurations. This genetic reshuffling process, called V(D)J recombination, yields the diversity of molecules necessary to combat the billions of different antigens they might encounter. The V, D, and J refer to different clusters of DNA sequences that follow specific rules of recombination.

While the products of recombination vary, the method does not. The fragments are spliced and then reassembled in a highly regulated process directed and controlled by a stretch of DNA (called a recombination signal sequence, or RSS) next to the gene fragment. The recombination process, the researchers show, relies on complex interactions among different parts of the signal sequences and the proteins that regulate them at key steps along the recombination pathway.

Each RSS is made up of three components: the nonamer, which controls the ability of proteins to bind to the gene fragments and initiate recombination; the heptamer, which directs the splicing of the gene fragment; and the spacer, which regulates how the gene fragments are recombined. Mutations in the DNA sequence of each of the three RSS components show that all play a critical role in the ability of the gene fragments to recombine appropriately.

While it has been established that spacers, as their name suggests, ensure that the space between the nonamer and heptamer is correct, the researchers show that spacers also regulate recombination activity by providing protein-binding sites along the DNA sequences that affect recombination. While the nonamer is the most important determinant of recombination, changes in the spacer, these researchers demonstrate, produced dramatic changes in the ability of the gene fragments to recombine.

Past studies have shown that recombination depends on the presence and sequence of specific nucleotides, but the quality of that recombination, the researchers say, can't be understood simply by analyzing those nucleotides in isolation. Generally speaking, highly conserved sequences have functional importance. But it would be a mistake, they suggest, to think that just because a nucleotide sequence isn't highly conserved, it's not biologically important. Using a computer model to predict how different protein-gene interactions affect recombination, the researchers demonstrate that a fuller understanding of the process depends on observing how all these elements—including those that aren't highly conserved—interact throughout the recombination process.

PMID: 14551906
Accession ID: PMC212689
License: CC BY
Last Updated: 2021-01-05 08:21:04
Retracted: no
Citation: PLoS Biol. 2003 Oct 13; 1(1):e8
==== Front
PLoS BiolPLoS BiolpbioplosbiolPLoS Biology1544-91731545-7885Public Library of Science San Francisco, USA 10.1371/journal.pbio.0000008FeatureBiotechnologyBotanyEcologyGenetics/Genomics/Gene TherapyPlant ScienceScience PolicyZeaGenetically Modified Corn— Environmental Benefits and Risks FeatureGewin Virginia 10 2003 13 10 2003 13 10 2003 1 1 e8Copyright: © 2003 Public Library of Science.2003This is an open-access article distributed under the terms of the Creative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are properly credited.To plant or not to plant. A discussion of the environmental benefits and risks of genetically modified crops
==== Body
Corn is one of humankind's earliest innovations. It was domesticated 10,000 years ago when humans learned to cross-pollinate plants and slowly turned a scraggly nondescript grass called teosinte into plump, productive modern corn (Figure 1). As needs change, so does plant breeding. Today, while biotech super-giants manipulate corn genetics to satisfy farmer desires and a global market, indigenous Mexican farmers do so to fulfill individual needs. Although the tools differ, the goal remains the same—to cultivate desirable traits.

Figure 1 Crossing for Kernels
Over time, selective breeding modifies teosinte's few fruitcases (left) into modern corn's rows of exposed kernels (right). (Photo courtesy of John Doebley.).

Plant breeding was once restricted to sexually compatible plants, and generations of offspring were selectively bred to create unique varieties. In fact, corn, along with rice and wheat—today's global crop staples—would not exist without such techniques. With the goal of ever-widening the pool of genetic diversity, conventional plant breeding has gotten more technologically savvy in recent years. For example, realizing that natural mutants often introduce valuable traits, scientists turned to chemicals and irradiation to speed the creation of mutants. From test-tube plants derived from sexually incompatible crosses to the use of molecular genetic markers to identify interesting hereditary traits, the divide between engineering and genetics was narrowing long before kingdom boundaries were crossed.

But when geneticists began to explore microorganisms for traits of interest—such as Bacillus thuringiensis (Bt) genes that produce a protein lethal to some crop pests—they triggered an uproar over ethical, scientific, and environmental concerns that continues today. (See Box 1.)

Box 1. Bt Technology

Bacillus thuringiensis, a soil bacterium, produces several crystal (Cry) protein toxins that destroy the gut of invading pests, such as larval caterpillars. So far, over 50 cry genes have been identified and found to affect insect orders differently.

Considered safe to humans, mammals, and most insects, Bt has been a popular pesticidal spray since the 1960s because it had little chance of unintended effects. Engineering the gene into corn, however, caused an unexpected public backlash. “We thought it was going to be the greatest thing since sliced bread,” says Guy Cardineau, agricultural biotechnologist at Arizona State University. “Here's a way to withstand insect pressure, eliminate the use of pesticides, and Bt spray was widely used in organic agriculture,” he adds. The Bt wrangle illustrates how differently a product and a process can be regarded.

After the expensive development process, today's concern is that broad-scale planting of Bt corn will render the toxin ineffective over time. Pests can gradually build resistance to any pesticide, and so the United States Environmental Protection Agency (EPA) requires that 20% of Bt field areas be planted to non-Bt corn to avoid such pressures. But humans have to follow the rules. A recent report from the Center for Science in the Public Interest shows that almost 20% of farmers in the United States Corn Belt are violating EPA standards by overplanting Bt corn, causing some to question the regulations and enforcement that will be necessary for certain GM crops.

Despite such discord, genetically modified (GM) crops have the fastest adoption rate of any new technology in global agriculture simply because farmers benefit directly from higher yields and lowered production costs. (See Table 1.) To date, the two most prevalent GM crops traits are Btderived insect resistance and herbicide resistance.

Table 1 Worldwide production of GM crops
Four crops account for most GM plantings: herbicide-tolerant soybeans (62%), insect-resistant corn (12.4%), insect-resistant cotton (6.8%), and canola (3%). Source: Summary Report on the Global Status of GM Crops by the International Service for the Acquisition of Agri-Biotech Applications (2002)

Since 1987, over 9,000 United States Animal and Plant Health Inspection Service (APHIS) permits have been issued to field-test GM crops. According to APHIS, corn is the most tested plant. The International Service for the Acquisition of Agri-Biotech Applications confirms that biotech corn is the second-most common GM crop (after soybean), with 12.4 million hectares planted in 2002. GM corn starch and soybean lecithin are just two of the ingredients already found in 70% of the processed food supply.

With future incarnations on the horizon, GM corn remains a lightening rod for debate. Embroiled in numerous controversies, corn has become biotech's boon and bane.

Benefits Emerging
As Danforth Center President Roger Beachy, the first to develop a virus-resistant tomato, describes it, the first-generation GM crops were intended to help farmers reduce not only the impact of pests, but also the use of agrochemicals in modern crop production–a legacy of the Green Revolution. After a decade of cultivation, environmental benefits are emerging.

Bt corn reduces the need for pesticides, and while the primary benefit comes largely during a heavy corn-borer infestation, an unpredictable event, a secondary effect is that beneficial insects fare much better under these conditions. The numbers are particularly impressive for Bt cotton: the spraying of almost 2 million pounds of pesticides—roughly 50% of previous usage—has been spared since the large-scale adoption of Bt cotton.

According to Leonard Gianessi, senior research associate at the National Center for Food and Agricultural Policy, farmers who adopt GM crops make more money in tougher times. Indeed, insect- and virus-resistance traits have already saved several industries. Bt cotton is credited with reviving the Alabama cotton industry, hard hit by uncontrollable bollworm infestations. Likewise, genetically engineered papaya, made resistant to the papaya ringspot virus, salvaged Hawaii's fifth largest crop industry.

Herbicide-resistant crops engendered a different reception. While GM critics acknowledge that the use of a more benign herbicide, called by its trade name Roundup, can have environmental benefits, the creation of a market monopoly is a key criticism. However, the increased planting of herbicide-resistant soybeans is an integral, but not sole, factor in the increased adoption of no-till farming— a strategy that reduces soil erosion.

Surprise benefits have also occurred. According to the recent International Council for Science (ICSU) review of GM crops, disease-resistant corn crops may have lower levels of mycotoxins, potentially carcinogenic compounds to humans. They result from fungal activity in insect-infested corn crops. With fewer insect holes in plant tissue, associated fungi are not able to invade and produce toxins.

While there is a growing amount of data documenting the intended environmental benefits of GM crops, the potential risks are more elusive.

Risky Business
After seven years of GM crop production and no apparent health effects, potential environmental risks—particularly gene flow into other species—have eclipsed food safety as a primary concern. As pollen and seeds move in the environment, they can transmit genetic traits to nearby crops or wild relatives. Many self-pollinating crops, such as wheat, barley, and potatoes, have a low frequency of gene flow, but the more promiscuous, such as sugar beets and corn, merit greater concern.

Determining where genes flow is a thriving research avenue, but the real question becomes “so what?” The risks associated with gene flow—such as creating weeds from introduced traits, reducing biodiversity, or harming nontarget species—are similar to those from conventionally bred crops. “I wouldn't dismiss the ecological concerns out of hand, but I think they can be exaggerated,” says Gabrielle Persley, the ICSU report author.

There are few instances of crop plants becoming weeds. Bred so intensely for hundreds of years, most crops cannot survive without human intervention. Increased weediness could be conveyed, however, if the plants are more fit or able to out-compete other crop species by producing more seed, by dispersing pollen or seed further, or by growing more vigorously in a specific environment. In fact, transgenic sunflowers can produce over 50% more seed than traditional varieties. Additionally, recent work shows that, compared to pollen, seeds are more likely to spread GM sugar beet genes into wild relatives in western Europe. Norman Ellstrand, plant geneticist at the University of California at Riverside, has shown that gene flow from many conventionally bred crops increases the weediness of nearby wild relatives.

For many domesticated crops, wild varieties do not exist in current areas of cultivation. Nevertheless, regions where crop species originated are particularly vulnerable to transgenic gene flow into local varieties, or landraces. Some fear that transgenic varieties with a competitive advantage might gradually displace valuable genetic diversity. For these reasons, transgenic corn is prohibited in Mexico, home to over 100 unique varieties.

Despite the ban, transgenes have been found in Mexican corn. “We have in several instances confirmed that there are transgenes in landraces of maize in Oaxaca,” says Ariel Alvarez-Morales, plant geneticist at the Mexican Center for Research and Advanced Studies (CINVESTAV) in Irapuato. The ramifications of this will not be known for some time, but Luis Herrera-Estrella, CINVESTAV's Director of Plant Biotechnology, is convinced that these single gene traits will be of little consequence to native Mexican varieties. “If Bt genes give an advantage to the farmer, they will keep growing it. In that case it will not be bad,” he says of dynamically changing landraces. “Gene flow has been occurring for 50 years from commercial lines to landraces.” While admitting this, Ellstrand points out that “if there are genes that you don't want to get into landraces—this shows how easily they can get there.” (See Box 2.)

Box 2. Pharma Corn
“The gene flow risk that keeps me awake at night is the possibility of hybridization between crops engineered to manufacture poisons and related crops intended for human consumption,” says plant geneticist Norman Ellstrand. Indeed, this application of GM crops seeks to turn corn into cost-effective pharmaceutical factories and may bear the mark of unacceptable risk. It is currently the subject of intense debate. An open-pollinated crop, corn is known for its promiscuity—making it more prone to gene flow risks than other crops. Genetic contamination takes on a whole new meaning when the escapable trait could produce proteins to treat diabetes or a hepatitis B vaccine.

Given that pharma corn demands multiple safety measures—including production in remote areas, separate farm equipment, delayed planting to offset pollination—many ask, “Why use corn?” “We know so much about corn genetics,” explains agricultural biotechnologist Guy Cardineau, “and it naturally lends itself to production with kernel packets of protein that can be stored indefinitely.” A number of scientists and United States food makers are not yet convinced that the benefits outweigh the risks and have joined environmental groups in questioning the use of pharma corn.

Over 130 acres of pharma crop field-tests were planted in 2002. Several products have moved on to clinical trials. Aware of concerns, the members of the influential Biotechnology Industry Organization decided last December to overturn its initial decision to remove pharma crops from the United States Corn Belt states and voluntarily police their use. A Colorado trial of corn producing a protein to treat cystic fibrosis recently began.

Indeed, unintended impacts are a primary concern. The potential risk to nontarget organisms took center stage when a 1999 paper in Nature suggested monarch butterfly populations might be adversely affected by Bt transgenes. Corrected by subsequent publications, the field experiments did not support original laboratory results. But effects on other nontarget organisms, such as soil microbes, remain a concern. When microbial genetics research uncovered how genes could be transferred between species in ways other than reproduction, so-called horizontal gene transfer, it not only explained why microorganisms were so diverse, but that microbes could potentially be endowed with GM plant DNA found in the soil. “Although a theoretical possibility, there is no evidence that it happens at any degree of frequency to be meaningful,” says Persley.

Opinions differ on this, however, and seem to follow the United States–European Union divide over the use of GM crops. Kaare Nielsen, microbial geneticist at Norway's University of Tromsø, is one of the few scientists to find examples of horizontal gene transfer. “There are actually very few studies and most of the ones conducted have been on first-generation plants,” Nielsen explains. Given that plant DNA can last in soil for over two years, Nielsen does not believe the possibility can be dismissed and argues that long-term studies are necessary. Work continues in this area in Europe.

The lack of baseline ecological data—even agreeing on what an appropriate baseline is—presents a substantial knowledge gap to environmental impact assessments. Scientists, including Nielsen, wonder whether there could be unexpected risk factors. Allison Snow, weed expert at Ohio State University, agrees with what many feel is the most important risk—the inability to anticipate all the effects. “Do we know all of the right questions we should be asking?” she wonders, adding, “Genes are complicated and can interact.” For these reasons, identifying factors that regulate weed and pest populations and determining how microbial community changes affect larger ecosystems are important areas of research.

Do Risks Differ for Developing Nations?
To two academicians that kindled the biotech revolution, the real GM risks lie in how science is misinterpreted and misused. In fact, much of the currently conducted basic research is not likely to be applied in the near future. Public concerns coupled with corporate consolidation created huge roadblocks, especially in getting the technology to developing nations. While Beachy blames the skyrocketing regulatory costs that “are due to regulators who have not put into context this technology and its relative safety,” Richard Jefferson, chairman and chief executive officer of the Center for the Application of Molecular Biology to International Agriculture in Australia, fears that innovation has been stifled by corporate short-sightedness. “The biggest risk is that [biotechnology] maintains itself as a monolithic, expensive industry with untenable entry barriers for smaller enterprises,” he says.

Indeed, when does the risk of not using available technology factor into the debate? (See Box 3.) Many scientists argue that genetic modification can help to ensure food security in developing countries, specifically in Africa. While more than 25% of the 2002 global biotech acreage was grown in countries such as Argentina, China, and India, there is little applied research on crops relevant to famine-prone African countries.

Box 3. Golden Rice
Current regulatory constraints have a choke-hold on innovations for genetic modifications that seek to improve subsistence crops, such as rice. Golden rice, yellowed in appearance because it is infused with the vitamin A precursor beta-carotene, could save thousands of malnourished people each year from blindness and the other vitamin A–deficiency diseases prevalent in Southeast Asia.

Intellectual property issues and opposition from anti-GM activists have confounded the development for years. Faced with patent issues and regulatory hurdles and costs, developer and academic researcher Ingo Potrykus formed an alliance with Syngenta (then AstraZeneca Corporation) to allow the free licensing of the patents to public research institutions for humanitarian use. In addition, farmers making less than US$10,000 will receive free golden rice seed.

After over a decade of work, golden rice is still not on the market. The retired Potrykus is determined to bring this technology to farmers once it passes regulatory field testing—an additional four-year delay that he feels is scientifically unnecessary. “Nobody can construct even a hypothetical risk to the environment from golden rice,” he says, adding that nutritional risks are nonexistent as well. He acknowledges, however, that field tests will be beneficial for acceptance of this and future bio-fortified products. “I have experienced so much support in these countries, I don't think it [the anti-GM lobby] will be able to stop this project once it passes regulation,” he says.

“Food security is not going to come from crops being marketed outside Africa, like wheat or rice,” says John Kilama, Uganda native and president of the Global Bioscience Development Institute. He points out that of traditional staple crops such as cow peas and millet, only cassava has merited some publicly-funded research. Beachy estimates that it takes between US$5 million and US$10 million to bring a GM crop to market. Given regulatory costs, neither industry nor universities can afford to develop products that do not have mass appeal. “If the crop is not worth that much to the seed market, it's likely that we'll never see the varieties because of the cost of regulation,” he says.

To ensure a return on research investments, with the regulatory costs often the biggest ticket item, developing blockbuster traits is a priority. “Given the diversity of environments and cropping systems, there are not many more blockbusters such as Roundup resistance in the wings,” says Jefferson. The alternative, he adds, is to make it cheaper to innovate local varieties in ways that are likely to gain public acceptance. (See Box 4.)

Box 4. Apomixis
One way to minimize the problems associated with gene flow is to introduce sterility, such that pollen cannot transmit information. Richard Jefferson has high hopes for an accessible, cheap way for farmers to produce genetically superior seeds, called apomixis.

But similar concepts have been floated before. The controversial terminator technology prevented gene flow, but it also outraged activists because it kept farmers from reusing seed.

Unlike terminator, apomixis is “germinator” technology—avoiding fertilization altogether by producing seeds without pollination. In effect, seeds can be natural clones of the mother, instead of a genetic exchange between mother and father. Therefore, hybrid quality can be maintained as farmers use seed year after year.

Although apomixis occurs naturally in about 400 plant species, Jefferson believes that it can be successfully developed as a useful trait in other crop plants. To ensure its widespread availability, Jefferson and collaborators pledged not to create restrictive patent rights that could block the development of apomixis.

“The Green Revolution largely bypassed Africa,” says Josette Lewis, biotechnology advisor for the United States Agency for International Development. Given monetary constraints that prevent access to many biotechnologies, many scientists worry that the Gene Revolution might as well. Looming trade issues coupled with food insecurity shape the debate in Africa. Caught between the United States and European Union trade disputes, sub-Saharan countries are eager to use any technology that will enhance production without jeopardizing trade.

Increasingly, industry is responding to the developing nations' needs. Both newly formed, the industry-focused African Agricultural Technology Foundation and the Public-Sector Intellectual Property Resource for Agriculture are attempting to ease cost restrictions and encourage access to current and future patents. By entering into such agreements, industries will be able to protect patent rights and commercially important markets. Such partnerships are already working. The Syngenta Foundation for Sustainable Agriculture is working together with the International Maize and Wheat Improvement Center (CIMMYT) and the Kenyan Agricultural Research Institute to overcome corn stemborer infestations in Kenya (Figure 2). “CIMMYT hopes to have a handful of local Bt corn varieties in farmers' fields by 2008,” says the admittedly ambitious Dave Hoisington, director of CIMMYT's Applied Biotechnology Center. Collaborations between public and private sectors may be the only way to navigate thorny patent issues and research crop varieties of interest to developing countries.

Figure 2 Biotech Bridge to Africa
In an effort to reduce corn stem-borer infestations, corporate and public researchers partner to develop local Bt corn varieties suitable for Kenya. (Photo courtesy of Dave Hoisington/CIMMYT.).

Conclusion
“Agricultural biotechnology is here to stay” read a recent opinion piece by Gianessi. No doubt he is correct. As genetic engineering continues to evolve, transgenic methods will become just one of many tools. In fact, some researchers are currently focusing their work on manipulating an organism's own genetic code to achieve desired traits.

Scientific inquiry will continue to weigh the risks and benefits of such technologies, realizing that there may never be enough evidence to ensure zero risk. Only with data will tolerable levels of environmental risks be determined—case by case.

Indeed, the level of risks and benefits may differ for developing nations, where decisions must be made in the face of food security concerns. To many scientists, the risks associated with forgoing genetic engineering far surpass any environmental risk associated with its use and further development. However, all stakeholders must have access to the tools in order to realize future benefits.

In the quest to feed the world, a few things are clear. Public outcries will continue to vet the need and use of genetic engineering. Private organizations will necessarily focus on research for profit, while exploring collaborative prospects. Public initiatives, however, will provide the critical bridge between science and global food security.

Although genetic engineering cannot be summarily accepted or rejected, any lack of scientific risk now doesn't negate future concerns. And, no matter what direction future research takes, corn will continue to be a bellwether crop.

Virginia Gewin is a freelance science journalist in Corvallis, Oregon, United States of America. E-mail: gewin@nasw.org.

Abbreviations
APHISUnited States Animal and Plant Health Inspection Service

BtBacillus thuringiensis

CIMMYTInternational Maize and Wheat Improvement Center

CINVESTAVCenter for Research and Advanced Studies

EPAEnvironmental Protection Agency

GMgenetically modified

ICSUInternational Council for Science.

PMID: 14551907
Accession ID: PMC212690
License: CC BY
Last Updated: 2021-01-05 08:25:30
Retracted: no
Citation: PLoS Biol. 2003 Oct 13; 1(1):e9
==== Front
PLoS BiolPLoS BiolpbioplosbiolPLoS Biology1544-91731545-7885Public Library of Science San Francisco, USA 10.1371/journal.pbio.0000009Community PageScience PolicyOut of the Way How the next copyright revolution can help the next scientific revolutionCommunity PageBrown Glenn Otis 10 2003 13 10 2003 13 10 2003 1 1 e9Copyright: © 2003 Public Library of Science.2003This is an open-access article distributed under the terms of the Creative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are properly credited.By default, all published works are copyrighted. Creative Commons provides means for authors to share their work more freely
==== Body
When did calling a lawyer become part of the scientific process? It hasn't officially, of course. But as a generation of researchers has grudgingly come to know, navigating the legal red tape of universities, corporations, and publishers is an inevitable part of the practice. Whether seeking access to information or sharing one's own findings with others, scientists increasingly find themselves having to ask an intermediary's permission.

This “ask first” culture has developed at just the moment when technology has opened vast new possibilities for collaboration and information-sharing. The timing is not coincidental. Policymakers, under the influence of lobbies defending pre-digital business models, have reacted to new technology with ever more extreme intellectual property laws. The result is a legal regime tailored to a powerful minority but ill-suited to a number of other constituencies—scientists and scholars chief among them—that thrive on openness. Worries over broad notions of “piracy” and “asset management” have insinuated themselves into fields where those terms, until recently, held no meaning.

The Public Library of Science (PLoS) is at the vanguard of a growing cross-disciplinary movement to counteract this trend by demonstrating that voluntary models of open publishing are not only viable, but crucial to scientific innovation. Yet PLoS’ goal of “immediate, unrestricted access to scientific ideas, methods, results, and conclusions” is not immediately compatible with the stringent rules of copyright, which apply fully and automatically to all published works, by default. The exercise of something less than full copyright requires, oddly, some legal tinkering—which is where Creative Commons, the organization I help manage, comes in.

Creative Commons, a 501 (c) (3) nonprofit corporation based at Stanford University in California, is led by a board of expert legal and technical thinkers. (Its chairman, Lawrence Lessig, a law professor at Stanford and a recipient of the Scientific American 50 Award in 2003, recently joined the PLoS board of directors.) Creative Commons was founded on the idea that some people prefer to share their works on more generous terms than standard copyright provides. The organization offers such authors an easy and clear way to announce these preferences. The goal is to help endeavors like PLoS, as well as individual authors, expand access to quality content online while reducing the legal friction and uncertainty of copyright law. In other words, Creative Commons offers legal tools to help clear permissions, once and for all. We help get the law out of science's way.

These tools are the Creative Commons licenses, a suite of form legal documents available for free on the Creative Commons website. Each license allows an author to retain his or her copyright while permitting certain uses of the work, on certain conditions: to declare “some rights reserved” as opposed to “all rights reserved.” From a simple menu, copyright holders mix and match their preferences: an attribution requirement; a prohibition on commercial reuse; a restriction on derivative works; or a “share-alike” provision that obligates licensees to offer any derivative works to the public on the terms they received. (PLoS has chosen the simplest and least restrictive of the licenses, permitting copying, as well as free commercial reuse and transformation, in exchange for simple attribution.)

Since the licenses’ launch in December 2002, nearly 800,000 Web pages (well over 1,000,000 discrete works) have been made available under Creative Commons licenses. Because they're free and can apply to any kind of copyrighted work, the licenses have been popular with Webloggers, teachers, novelists, musicians, photographers, and hobbyists. Many institutional adopters, too, have used the licenses to facilitate innovative publishing techniques, particularly in the sciences.

The Massachusetts Institute of Technology's Open Courseware project publishes materials from its university courses under a version of the licenses, inviting students and educators from around the world to reuse them royalty-free. Rice University's Connexions project, an interactive tool that helps instructors build courses and texts from a collective knowledge repository, requires authors to license their contributions for free reuse in return for authorial attribution. The American Museum of Natural History's Biodiversity Commons will soon use the licenses to facilitate search across a broad collection of conservation databases and websites.

Like PLoS, all of these projects use Creative Commons licenses to simplify and streamline the process of rights clearance. But the licenses also serve another critical function: they formalize the collaborative ethos of the scientific and academic communities in a language that legal intermediaries cannot quarrel with. This standardization also helps otherwise disparate communities, whether across disciplines or geographic boundaries, to agree in advance on the rules for sharing.

Creative Commons is now considering expanding into other fields where the law has begun to restrict open research: scientific data and patents, in particular. With a portion of a new US$1 million grant from the Hewlett Foundation (putting our total of funding received at over US$3 million), we hope to build the Science Commons, a branch of the organization dedicated to bringing a measure of reason, and restraint, to the legal thicket that has grown around scientific research.

Like PLoS, Creative Commons’ goals and methods are designed to make the most of the opportunities created by new communications technology. But, also like PLoS, our inspiration reflects the wisdom and optimism of the Enlightenment as much as that of the Digital Age. We are trying to restore the sense of legal moderation that policymakers of a bygone era, heavily influenced by the philosophy of the first scientific revolution, understood would “promote the progress of science and the useful arts,” as the U.S. Constitution puts it.

“Knowledge [is] not the personal property of its discoverer, but the common property of all,” wrote Benjamin Franklin, the great cosmopolitan, polymath, and patron saint of innovation. As we enjoy great advantages from the inventions of others, we should be glad of an opportunity to serve others by any invention of ours, and this we should do freely and generously.”

Franklin, who knew a thing or two about both publishing and science, never practiced law.

Glenn Otis Brown is the executive director of Creative Commons (http://www.creativecommons.org), located in Palo Alto, California, United States of America. E-mail: glenn@creativecommons.org.

PMID: 14551908
Accession ID: PMC212691
License: CC BY
Last Updated: 2021-01-05 08:21:03
Retracted: no
Citation: PLoS Biol. 2003 Oct 13; 1(1):e10
==== Front
PLoS BiolPLoS BiolpbioplosbiolPLoS Biology1544-91731545-7885Public Library of Science San Francisco, USA 10.1371/journal.pbio.0000010Research ArticleBioinformatics/Computational BiologyCancer BiologyCell BiologyDevelopmentMolecular Biology/Structural BiologyXenopusThe Roles of APC and Axin Derived from Experimental and Theoretical Analysis of the Wnt Pathway Mathematical Modeling of the Wnt PathwayLee Ethan 
1

3
Salic Adrian 
1
Krüger Roland 
2
Heinrich Reinhart reinhart_heinrich@hms.harvard.edu
2
Kirschner Marc W marc@hms.harvard.edu
1
1Department of Cell Biology, Harvard Medical SchoolBoston, MassachusettsUnited States of America2Department of Theoretical Biophysics, Institute of BiologyHumboldt University Berlin, BerlinGermany3Department of Cell and Developmental Biology, Vanderbilt University Medical CenterNashville, TennesseeUnited States of America10 2003 13 10 2003 13 10 2003 1 1 e1020 6 2003 1 8 2003 Copyright: © 2003 Lee et al.2003This is an open-access article distributed under the terms of the Creative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are properly credited.
Mathematical Modeling Predicts How Proteins Affect Cellular Communication 
Wnt signaling plays an important role in both oncogenesis and development. Activation of the Wnt pathway results in stabilization of the transcriptional coactivator β-catenin. Recent studies have demonstrated that axin, which coordinates β-catenin degradation, is itself degraded. Although the key molecules required for transducing a Wnt signal have been identified, a quantitative understanding of this pathway has been lacking. We have developed a mathematical model for the canonical Wnt pathway that describes the interactions among the core components: Wnt, Frizzled, Dishevelled, GSK3β, APC, axin, β-catenin, and TCF. Using a system of differential equations, the model incorporates the kinetics of protein–protein interactions, protein synthesis/degradation, and phosphorylation/dephosphorylation. We initially defined a reference state of kinetic, thermodynamic, and flux data from experiments using Xenopus extracts. Predictions based on the analysis of the reference state were used iteratively to develop a more refined model from which we analyzed the effects of prolonged and transient Wnt stimulation on β-catenin and axin turnover. We predict several unusual features of the Wnt pathway, some of which we tested experimentally. An insight from our model, which we confirmed experimentally, is that the two scaffold proteins axin and APC promote the formation of degradation complexes in very different ways. We can also explain the importance of axin degradation in amplifying and sharpening the Wnt signal, and we show that the dependence of axin degradation on APC is an essential part of an unappreciated regulatory loop that prevents the accumulation of β-catenin at decreased APC concentrations. By applying control analysis to our mathematical model, we demonstrate the modular design, sensitivity, and robustness of the Wnt pathway and derive an explicit expression for tumor suppression and oncogenicity.

Wnt signaling is important in both oncogenesis and development. Mathematical modeling predicts several unusual features of the Wnt pathway, some of which are tested experimentally
==== Body
Introduction
Considerable effort employing biochemistry, genetics, and pharmacology has been invested in identifying the web of interactions that characterize signal transduction pathways in metazoan organisms. Several conclusions can be drawn from these efforts. Despite the large number of receptors, ligands, and downstream targets, the number of signal transduction pathways in metazoans is relatively small, arguably less than 20 (Gerhart 1999). This limited diversity occurs despite large numbers of different organisms, cell types, states of growth, and differentiation, as well as sexual dimorphism in biology. Remarkably, these pathways are highly conserved, some among all eukaryotes, most among all metazoans. Whereas signaling pathways differ in detail, it is not clear whether these differences are functionally significant. Conservation in the face of diversity of function raises the question of whether the behaviors of the pathway are in reality as similar as they seem when one compares more quantitative aspects of the signals and responses, such as amplitude, duration, and flux (Heinrich et al. 2002). Finally, the structure and design of the pathways are themselves a mystery. Is the structure of these conserved pathways so deeply embedded in other conserved process that it is difficult to change any interaction, or does conservation imply continuous selection for function (Gerhart and Kirschner 1997)?

Many of these questions require a more quantitative understanding of the behavior of signaling pathways. Such information is rarely available. Most mathematical models have to be satisfied with a general conceptual understanding and are seldom testable, as most parameters must be assumed or inferred. It is partly for this reason that such theoretical efforts up to now have had limited impact on experimentalists, who prefer powerful qualitative tools to construct logical and formal models of pathway structures. Mathematical modeling is more advanced for metabolic networks, where the pathways have been known for more than a half-century and where more kinetic data have been available, including more recent data on in vivo dynamics (Heinrich and Schuster 1996). To develop a better quantitative understanding of a signal transduction pathway, we have recreated a more accessible system for biochemical study. The Wnt signaling pathway downstream of its immediate cytoplasmic mediator, Dishevelled (Dsh), can be reconstituted in frog egg extracts. The readout of the pathway is the rate of degradation of the transcriptional coactivator, β-catenin. We chose the Wnt pathway because it is active in the early Xenopus embryo, it is widely used in many different contexts in development, and it is also very important in human cancer. Although the design features of the Wnt pathway are highly conserved in evolution, it is not clear what purposes those features serve. This paper is in part an answer to that question.

The pivotal player in Wnt signaling is the scaffold protein axin, which is required for the constitutive degradation of β-catenin. Axin coordinates the assembly of a large complex that includes the glycogen synthase kinase 3β (GSK3β); another scaffold protein, adenomatous polyposis coli (APC); and the negative regulators Dsh and GSK3β-binding protein (glycogen synthase kinase-binding protein [GBP]/Frat). Binding of Wnt to its receptor, Frizzled, activates Dsh through an as-yet-unknown process. In the absence of Wnt, GSK3β bound to axin phosphorylates β-catenin bound to both axin and APC. Phosphorylated β-catenin is a substrate for ubiquitination and subsequent degradation through the F-box protein β-TRCP, which is part of an SCF ubiquitin ligase complex. In the presence of the Wnt signal, the activated Dsh protein binds to axin and, through bound GBP, inhibits β-catenin phosphorylation; this inhibits its ubiquitination and consequent degradation. The buildup in β-catenin in the presence of a Wnt signal leads to transcription of specific genes.

Numerous questions arise from this general model. Why are two scaffold proteins, APC and axin, both necessary? Do their roles differ? Recently it has been discovered that axin, like β-catenin, is an unstable protein (Yamamoto et al. 1999; Tolwinski et al. 2003). In recent work (unpublished data), we have further described the conditions under which axin is unstable. We ask here what role axin instability plays in the behavior of the Wnt pathway and in the responsiveness of the pathway to the Wnt signal? Beyond these mechanistic questions are important biological ones that lie beyond the scope of this work but that may be raised by some of the findings here. For example, mutations in APC seem to play a particularly important role in colorectal cancer; is the peculiar sensitivity to APC mutations in the colonic epithelium understandable in terms of how the pathway performs in that tissue? Similarly, GSK3β is also essential but not commonly mutated in colorectal cancer; why is that the case? No one has purified a discrete complex containing all the major players in the Wnt pathway arrayed on the axin–APC scaffolds, suggesting that the pathway might be affected by nonproductive titration of components by subcomplexes. If this is a problem, how is it avoided? The Wnt pathway is likely present in all cell types, and yet several of its constituents are used in other pathways; how is crosstalk or interference in other pathways avoided? As we set out to produce a realistic kinetic model of the Wnt pathway, we encountered other questions. For example, quantitative measurements led to the unusual finding that axin is present at very low concentrations. Is there a satisfactory explanation of this fact and of other, previously unexplained, features of the pathway? We are aware that some of the answers to specific questions could lie in unknown components or unknown interactions among known components. We were under no illusions that we could accommodate all known interactions in a model at this time or that we already knew all we need to know to construct such a model. For this reason we have asked a more modest question—whether the properties of the core pathway, as presently understood, can provide insight into important questions not yet answered or not yet clearly raised.

To answer such questions, we collected what we initially thought were sufficient quantitative data on rates, affinities, and fluxes to derive a reference state model of the Wnt pathway in this system. The provisional reference state model reflected most of the known properties of the system, but from this model we identified several rates and affinity constants whose values were critical to the behavior of the model. We then went back and measured these. Thus this paper contains a reference model, a large number of experimental measurements needed to define this model, theoretical predictions, and experimental tests of those predictions, where possible. A general test of the validity of the model is its predictive ability under a wide range of conditions. From this analysis, several unexpected properties emerged with significance for understanding the biological function of the Wnt pathway.

Results
A Proposed Kinetic Pathway
The model was based on the reaction scheme shown in Figure 1. A few steps are labeled, such as the synthesis of axin and β-catenin, the degradation of axin, the axin-independent (basal) and axin-dependent degradation of β-catenin, as well as the critical cycle involved in the phosphorylation of β-catenin for degradation (Destruction Core Cycle). The output is the formation of the β-catenin/T-cell factor (TCF) complex and the input is the Wnt signal. Although many proteins interact with the Wnt pathway, we have focused only on core components known to be necessary for mediating a Wnt signal in most contexts. These core proteins include GSK3β, protein phosphatase 2A (PP2A), β-catenin, APC, axin, Dsh, TCF, and Wnt. The reactions incorporated into our model include protein synthesis/degradation, protein phosphorylation/dephosphorylation, and the assembly/disassembly of protein complexes (Figure 1, solid arrows). Reactions mediated by proteins that activate a process are represented with broken arrows: (1) activation of Dsh by Wnt (step 1), (2) activation of the release of GSK3β from APC/axin/GSK3β by Dsh (step 3), and (3) activation of APC-dependent axin degradation (step 15). The reactions and components in blue are concerned with additional features of the pathway, as discussed below.

Figure 1 Reaction Scheme for Wnt Signaling
The reaction steps of the Wnt pathway are numbered 1 to 19. Protein complexes are denoted by the names of their components, separated by a slash and enclosed in brackets. Phosphorylated components are marked by an asterisk. Single-headed solid arrows characterize reactions taking place only in the indicated direction. Double-headed arrows denote binding equilibria. Blue arrows mark reactions that have only been taken into account when studying the effect of high axin concentrations. Broken arrows represent activation of Dsh by the Wnt ligand (step 1), Dsh-mediated initiation of the release of GSK3β from the destruction complex (step 3), and APC-mediated degradation of axin (step 15). The broken arrows indicate that the components mediate but do not participate stoichiometrically in the reaction scheme. The irreversible reactions 2, 4, 5, 9–11, and 13 are unimolecular, and reactions 6, 7, 8, 16, and 17 are reversible binding steps. The individual reactions and their role in the Wnt pathway are explained in the text.

The centerpiece of the model is the formation of the unstable core complexes involved in β-catenin phosphorylation and subsequent destruction. In addition to β-catenin, this set of complexes contains GSK3β and the scaffold proteins APC and axin. The complexes assemble in several steps: (1) binding of axin to APC (forward reaction of step 7); (2) binding of GSK3β (forward reaction of step 6); (3) phosphorylation of axin and APC by GSK3β (step 4). Dephosphorylation of the core complex (step 5) is mediated by PP2A. The first step in β-catenin degradation is its binding to APC*/axin*/GSK3β (step 8), after which it is phosphorylated by GSK3β (step 9) and released from the complex (step 10). Our model assumes that the phosphorylation of β-catenin by GSK3β is negligible in the absence of axin. Indeed, recent work indicates that axin stimulates the phosphorylation of β-catenin by GSK3β at least 24,000-fold (Dajani et al. 2003). Free, phosphorylated β-catenin is rapidly polyubiquitinated and degraded by the SCF complex and the proteasome, respectively (step 11).

The dynamic properties of the model, such as the flux through the pathway, are also affected by binding of β-catenin to other partners, such as TCF (step 16) and free APC (step 17). In special cases (high axin concentrations), the flux through the system is affected by the binding of axin to GSK3β (step 19) as well as β-catenin (step 18). We have previously shown experimentally that TCF reduces the rate of β-catenin degradation (Lee et al. 2001). Turnover of β-catenin (steps 11, 12, and 13) and axin (steps 14 and 15) are included in our model, but since biochemical experiments in Xenopus egg extracts indicate that the turnover of GSK3β, Dsh, and TCF is relatively slow (no detectable degradation after 3 h at room temperature; unpublished data), the synthesis and degradation of these proteins are not explicitly modeled. The activation of the pathway in vivo, which results in the stabilization of β-catenin, is initiated by binding of Wnt ligands to Frizzled receptors and the subsequent transition of Dsh from its inactive form (Dshi) to its active form (Dsha). Since these events are still poorly defined, both processes have been combined in step 1. Interaction of Dsha with the nonphosphorylated complex APC/axin/GSK3β (step 3) activates the release of GSK3β . This latter process requires the activity of the GBP/Frat (not shown on our diagram). Deactivation of Dsha occurs through an as-yet-unidentified mechanism (step 2).

Analytical Description
The mathematical analysis is based on a series of balance equations that describe the concentrations and complexes of proteins in the Wnt pathway, as depicted in Figure 1. The set of variables and the set of 15 differential equations we obtained are given in Table S1, and Dataset S1, respectively (Equations [A-1]–[A-15]). Stimulation of the pathway by Wnt is described by a time-dependent function, Wnt(t). Since Dsh, TCF, and GSK3β are degraded very slowly, we assume that their concentrations remain constant throughout the timecourse of a Wnt signaling event. The conservation equations for Dsh, TCF, and GSK3β are as follows:
  
  
  Symbols with the superscript "0" denote total concentrations.


Since the concentration of axin is very low (see below) compared to the concentration of GSK3β, we replaced Equation (3) with the simple relationship GSK3β
0 = GSK3β. Similarly, we omitted the concentration of complexes containing axin in the conservation relationship for APC, which leads to the following equation:
  


We will, however, take into account the contribution of axin-containing complexes for GSK3β and APC conservation equations when we later consider the effect of large increases in axin concentration.

The simplest possible equation was chosen to describe the kinetics of each individual reaction. Synthesis of β-catenin and axin are described by constant rates ν
i. Unimolecular reactions are assumed to be irreversible and are described by linear rate equations ν
i = ki · Xj, where ki denotes the first-order rate constant and Xj denotes the concentration of the reactants. Reversible binding steps (double-headed arrows in Figure 1) are described by the equation ν
i = k+iXjYl − k−i(Xj
.
Yl), where Xj and Yl denote the concentrations of the binding partners and (Xj
.
Yl) the concentration of their complex. The Dsh-mediated release of GSK3β from the destruction complex is described by an irreversible reaction that is bimolecular in the concentrations of Dsh and the degradation complex. The model is simplified by assuming that the reversible binding steps between axin, β-catenin, APC, and TCF are very fast, such that the corresponding protein complexes are in rapid equilibrium, so that only the dissociation constants Ki = k
−i/k
+i are considered in the kinetic description of these steps. The conservation equations and the binding equilibria reduce the number of independent dynamic variables. Accordingly, the original set of 15 differential equations is transformed into a set of only seven ordinary differential equations coupled to four conservation equations and four relationships for binding equilibria. For a detailed mathematical description of the model and the procedure for reducing the number of systems variables, see Dataset S1.

Experimental Evaluation of the Reference and Stimulated States
We define the reference state as the absence of Wnt signaling (Wnt = 0). In this unstimulated stationary state, Dsh is inactive and does not affect the degradation complex. β-Catenin concentration is kept low by continuous phosphorylation and degradation. The reference state can be characterized by the special values for its rate constants, its equilibrium constants, and its conservation quantities. If one can obtain values for all of these system parameters, the model equations should allow for a straightforward calculation of the variables in the reference state. Currently, we have experimental data for many of these parameters (see below). For the remaining system parameters that were not directly measured, we were able to derive numbers based on experimental data of steady-state concentrations and fluxes. A number of parameters were set such that the results of the model were in agreement with previous experimental data, specifically with the experimentally determined rate of β-catenin degradation (Salic et al. 2000; Lee et al. 2001). Finally, a few parameters had to be estimated; the constraint used was that the resulting model should be compatible with the steady-state and flux values. Table 1 lists the numeric values of all of the input quantities of the model. These quantities are either specific parameters, such as dissociation constants, or systemic properties, such as steady-state concentrations or fluxes, from which the other parameters have been derived. Both types of input quantities include experimental data as well as estimated values. The specific numerical values affect the model to differing degrees. In a later section, we analyze the effects of changing the values of the parameters around their reference numbers. The types of input data used for our modeling can be divided into five groups.

Table 1 Numeric Values of Input Quantities of the Model for the Reference State
The data are grouped into concentrations of pathway components, dissociation constants of protein complexes, concentration ratios, fluxes and flux ratios, and characteristic times of selected processes. Experimental evidence for these data is discussed in the text. From these data, the following rates and rate constants are calculated: ν
12 = 0.42 nM · min−1 (rate of β-catenin synthesis), ν
14 = 8.2 · 10−5 · nM min−1 (rate of axin synthesis), k
4 = 0.27 min−1, k
5 = 0.13 min−1, k
6 = 9.1 · 10−2 nM−1 · min−1, k−
6 = 0.91 · nM−1 · min−1, k
9 = 210 min−1, k
10 = 210 min−1, k
11 = 0.42 min−1, k
13 = 2.6 · 10−4 min−1, k
15 = 0.17 · min−1. See Table S2, found at http://dx.doi.org/10.1371/journal.pbio.0000010.st002, for more precise numbers used in the calculations


Bold: Measured values,
Italics: Estimated values

The first group of input data contains both total concentrations (Dsh
0, APC
0, TCF
0, and GSK3β
0) and steady-state concentrations (Axin
0, β-catenin
0, β-catenin*). The total concentrations of Dsh, TCF, GSK3β, axin, β-catenin, and APC in Xenopus egg extract were determined experimentally using Western blot analysis by comparing the intensity of the signal to that of known amounts of recombinant protein. The concentration of phosphorylated β-catenin w as estimated because we have not been able to directly determine its level in extracts. However, we estimate that this value is small compared to that of nonphosphorylated β-catenin for the following reasons: (1) Addition of axin to Xenopus extracts dramatically increases the rate of β-catenin degradation. Since the role of axin is to promote phosphorylation of β-catenin, which is subsequently degraded, this would suggest that normally a significant pool of β-catenin exists in the nonphosphorylated form. (2) Western blot analysis of Xenopus extracts demonstrates that only a small percentage (<10%) of total β-catenin can be detected as migrating with a slower mobility, which likely represents the phosphorylated form of β-catenin.

The second group of input data was experimentally obtained from measurements of rates of dissociation of protein complexes. Binding constants were calculated based on the assumption that association rates approached that of the diffusion limits for a typical protein in an aqueous solution. The ratio K
17/K
8 = 10 of the dissociation constants characterizing the binding of β-catenin to APC and APC*/axin*/GSK3β, respectively, is based on previous experimental results demonstrating that β-catenin has a 10-fold lower affinity for nonphosphorylated compared to phosphorylated APC (Salic et al. 2000). In addition, we have shown experimentally (unpublished data; see Materials and Methods) that phosphorylated β-catenin dissociates from axin more rapidly (reaction 10) than nonphosphorylated β-catenin. Once phosphorylated, β-catenin will thus dissociate from the axin complex and undergo polyubiquitination and proteolysis.

The third group of input data consists of the two concentration ratios in the Destruction Core Cycle for complexes that either contain or lack β-catenin. The concentration ratio for the complexes that lack β-catenin is represented by the ratio of its phosphorylated versus nonphosphorylated forms and reflects the relative activities of its kinase(s) and phosphatase(s), respectively. By contrast, the concentration ratio of the two β-catenin-containing degradation complexes represents the relative activities of β-catenin phosphorylation and the rate of release of phosphorylated β-catenin from the complex. These parameters were chosen rather arbitrarily to indicate roughly equal kinase and phosphatase activities and yielded realistic values for the overall fluxes, given the known concentrations and kinetic rate constants.

The fourth group of data includes the steady state flux ν
11 for the degradation of β-catenin via the Wnt pathway and the flux ratio ν
13
/
ν
11 describing the extent to which β-catenin is degraded via non-Wnt mechanisms (e.g., via Siah-1 and presenilin [Liu et al. 2001; Matsuzawa and Reed 2001; Kang et al. 2002]). We have now measured this Wnt pathway–independent degradation in Xenopus extracts (see Materials and Methods; value shown in Table 1).

The final group of input data consists of the characteristic time constant (τ) of selected processes. This is the time it takes for the concentration to drop to 1/e of its initial value. These characteristic times include τK
.
P = 1/(k
4 + k
5) for the kinase/phosphatase cycle that mediates phosphorylation/dephosphorylation of both APC and axin in the degradation complex (steps 4 and 5), τGSK3β
.
ass = 1 / (k
6
GSK3β + k
−6) for the binding equilibrium of GSK3β with the APC/axin complex (step 6), and τax
.
deg for axin degradation (step 15). Values for the rate of axin degradation were determined directly from experiments performed in Xenopus egg extracts (unpublished data). Experiments to determine the rate of APC and axin dephosphorylation (τK
.
P ≈ 2.5 min) were performed using in vitro 32P-labeled recombinant APC and axin. Radiolabeled proteins were added to Xenopus egg extracts, and the loss of radioactivity over time was assessed by SDS-PAGE and autoradiography (Salic et al. 2000). The legend to Table 1 contains the values of rate constants calculated from the input quantities using the described system of equations. The values of all variables in the reference state are listed in the first column of Table 2. These values represent the steady state solutions of system equations using the data in Table 1 as input quantities with the value of Wnt set at Wnt = 0.

Table 2 Steady-State Concentrations of Pathway Compounds in the Reference State and in the Standard Stimulated State
Calculation of the concentrations is performed by the systems equations (see Dataset S1) under steady-state conditions. For the reference state (W = 0), the corresponding parameters given in Table 1 are used. Values marked by “#” represent steady-state concentrations, which also appear in Table 1. The additional input quantities required for the calculation of the standard stimulated state (W = 1) are taken as follows: Dsh a / Dsh i = k
1
/ k
2 = 10, ν
−6
/
ν
3
= k
−6
/ (k
3
Dsha) = 0.2, and τDsh
.
act  = 1 / (k
1
+ k
2) = 5 min. This yields the following values for rate constants: k
1 = 0.18 min−1, k
2 = 1.8 · 10−2 min−1, k
3 = 5.0 · 10−2 nM−1 · s−1


Using the reference state as a starting point, we consider other stationary states that are attained when the pathway is permanently stimulated. To describe the strength of Wnt stimulation, we introduce a dimensionless quantity W = Wnt/Wnt
0 that represents the ratio of the Wnt concentration with respect to its concentration Wnt
0 in a “standard” stimulated (signaling) state. W = 0 and W = 1 characterize the reference state and a standard stimulated state, respectively, with the hyperstimulated state defined as W > 1. In order to calculate concentrations in the standard stimulated state, additional input quantities are required. These include the ratio of the active and inactive forms of Dsh (Dsha/Dshi), the relation between non-Dsh-mediated and Dsh-mediated release of GSK3β from the destruction complex (the flux ratio ν
−
6/ν
3), and the characteristic time for the Dsh activation/inactivation cycle (τDsh
.
act). These values are not at present measurable. The values for these input quantities are listed in the legend of Table 2. In a later section, we analyze the effects of changes in these additional input quantities.

By setting W = 1 and fixing all other parameters, we arrive at steady-state solutions of the systems equations (see Dataset S1, Equations. [A-1]–[A-15]), which yield the numerical variables for the standard stimulated state (listed in the second column of Table 2). A comparison of this state with the reference state shows that the concentration of free nonphosphorylated β-catenin increases by a factor of approximately 6, from 25 to 153 nM. Upon Wnt stimulation, the free phosphorylated β-catenin concentration decreases by 8%, from 1 nM to 0.92 nM. The increase in β-catenin levels reflects the decrease in its degradation caused by the reduction in the ability of GSK3β to phosphorylate it. The concentration of the β-catenin/TCF complex increases by a factor of 1.8. The large increase in β-catenin concentration shifts the binding equilibrium between APC and β-catenin and the concentration of free APC falls slightly. Total axin concentration decreased by a factor of 2.7 upon Wnt stimulation since addition of Dsh decreases the concentration of the various axin containing complexes. Remarkably, the steady-state concentration of free axin is constant during the transition from W = 0 to W = 1. This is due to the fact that under steady-state conditions, the rate of axin synthesis equals its degradation; the rate of synthesis (ν
14) is a fixed value and the rate of degradation depends solely on the concentration of free axin (and independent of other parameters such as binding constants and strength of the Wnt signal).

As expected, simulations of increasing Wnt activation (0 ≤ W ≤ 1.4) on the steady-state concentrations of β-catenin and axin reveal a nearly hyperbolic saturation of increasing concentrations of nonphosphorylated and total β-catenin with increasing strength of Wnt stimulation. Furthermore, Wnt stimulation affects the steady-state concentrations of axin and β-catenin in an opposite direction (see Figure S1).

β-Catenin Degradation: Comparison of Theory and Experiment
To test whether the mathematical model represented the Wnt pathway under a variety of conditions, we ran through a series of simulations, all of which used the same set of parameters. From these we calculated simulated timecourses for β-catenin degradation under a range of different conditions (increased axin concentration, increased Dsha concentration, inhibition of GSK3β, increased TCF concentration) (Figure 2A). We then tested the results using the previously described biochemical system (Salic et al. 2000; Lee et al. 2001), adding purified proteins or compounds at t = 0 (Figure 2B). Simulations and experimental results are each shown as plots of total β-catenin concentration versus time. The agreement between theory and experiment is excellent.

Figure 2 Kinetics of β-Catenin Degradation: Simulation and Experimental Results
(A) Simulated timecourses of β-catenin degradation. The straight line for t < 0 corresponds to the reference state of β-catenin using the parameters given in the legends of Table 1 and 2. In vitro conditions are simulated by switching off synthesis of β-catenin and axin (ν
12 = 0, ν
14 = 0 for t ≥ 0). Curve a: reference case (no addition of further compounds); curve b: addition of 0.2 nM axin; curve c: addition of 1 μM activated Dsh (deactivation of Dsh was neglected, k
2 = 0); curve d: inhibition of GSK3β (simulated by setting k
4 = 0, k
9 = 0); curve e: addition of 1μM TCF. Addition of compounds (axin, Dsh, TCF) and inhibition of GSK3β was performed at t = 0.

(B) Experimental timecourse of β-catenin degradation in Xenopus egg extracts in the presence of buffer (curve a′), axin (curve b′: 10 nM), Dsh (curve c′: 1 μM), Li+ (curve d′: 25 mM), or Tcf3 (curve e′: 1 μM).

The straight line for t < 0 represents the reference state. The simulated reference state curve (Figure 2A, curve a) for β-catenin degradation is calculated for t > 0, at which there is an absence of protein synthesis for axin (ν
14 = 0) and β-catenin (ν
12 = 0). This reference curve is in close agreement with our experimental data (Figure 2B, curve a′) with identical half-lives for β-catenin degradation (theoretical value of t
½ = 60.2 min versus experimental value of t
½ = 60 min). We examined a new state, where we have increased the amount of endogenous axin (0.02 nM) by 0.2 nM. As shown in Figure 2A, curve b, the additional axin markedly accelerated β-catenin degradation (t
½ = 11.8 min) in agreement with the experimentally obtained values (Figure 2B, curve b′; t
½ = 12 min). Theoretically, the effect of axin on β-catenin degradation is primarily due to the large concentration difference between the two scaffold proteins, APC and axin. Owing to the high concentration of APC, an increase in axin concentration results in a sharp increase in the concentration of the APC/axin complex, thereby accelerating β-catenin binding to the destruction complex.

Curve d in Figure 2 shows the effect of inhibiting GSK3β on β-catenin degradation. This effect is produced in the simulation by inhibiting GSK3β activity (steps 4 and 9). Only a small fraction of β-catenin (phosphorylated β-catenin) is available for degradation after complete inhibition of β-catenin phosphorylation (step 9), so inhibition is rapid. This is in complete agreement with our experimental data in which degradation is essentially blocked after inhibiting GSK3β activity by lithium (Figure 2B, curve d′). Curve e in Figure 2A predicts that β-catenin degradation is strongly inhibited after the addition of 1 μM TCF. Previously we have shown that β-catenin is sequestered by TCF, thereby resulting in a significant decrease in free β-catenin (Lee et al. 2001). The addition of TCF would be expected to decrease the rate of β-catenin phosphorylation (step 9) and subsequently β-catenin degradation. This is also seen experimentally (Figure 2B, curve e′).

The immediate inhibition by LiCl is in contrast with the action of Dsh that inhibits only after a significant delay. We were intrigued by the theoretical biphasic degradation curves of β-catenin in the presence of Dsha, as well as the experimental support for it (Figure 2A and 2B, curves c and c′). In both cases, there is an initial rapid decrease in β-catenin in the first 30 min to 1 h, followed by a much slower decrease. Such a feature should allow us to distinguish mechanistic details of complex formation. Experimentally, the biphasic nature of Dsh activity is not due to a delay in Dsh activation upon its addition to the Xenopus extracts since we see the same effect with Dsh protein that has been “activated” with extracts prior to its use in our degradation assay. As shown in Table 1, the characteristic time τK
.
P of phosphorylation and dephosphorylation of APC and axin in the destruction complex is relatively slow (2.5 min), and it therefore takes 5 min for 75% of the complex to be dephosphorylated. If Dsha acted only on the dephosphorylated complex (through step 3) to remove GSK3β and thus block phosphorylation of the complex, then we would predict the biphasic kinetics shown in Figure 2A, curve c. These data suggest that Dsh inhibits the phosphorylation of the scaffold complex by GSK3β, but does not inhibit the phosphorylation of β-catenin. When Dsh binds, the complex can go around many times binding and phosphorylating β-catenin before it dissociates and is inhibited by Dsh. One hour after the addition of Dsh, β-catenin degradation is significantly inhibited due to the removal of a significant pool of GSK3β from the degradation complex over time (through the action of Dsh). As a result, the scaffold protein axin is dephosphorylated by the phosphatase (step 5) that remains bound to the degradation complex. Dephosphorylated axin is rapidly ubiquitinated and degraded when the β-catenin degradation normally stops. The small decrease in β-catenin levels in Figure 2, curve c, after a 1 h incubation with Dsh, is due to degradation of β-catenin via nonWnt pathway mechanisms (see Table 1) that we have incorporated into our model.

To test this prediction beyond consistency with experimental data, we performed an experiment in which Dsh was either preincubated with extract before or added at the same time as radiolabeled β-catenin (Figure 3). If β-catenin and Dsh are added at the same time, there is an initial rapid loss of β-catenin (Figure 3, curve b) followed by pronounced inhibition of degradation after 1 h. This initial rapid loss is consistent with Dsh acting on a subpopulation of degradation complexes (presumably the unphosphorylated forms). Strikingly, preincubation with Dsh prior to the addition of radiolabeled β-catenin (Figure 3, curve a) results in immediate action of Dsh. We interpret this result to simply reflect the fact that over time in the preincubated extract Dsh can remove GSK3β from the degradation complexes, thereby enhancing the activity of the phosphatase and, as a result, promoting the degradation of axin and inhibition of β-catenin degradation. The small decrease in β-catenin levels at t > 2 h in both curves a and b again suggests the existence of a slow degradation process mediated by non-Wnt pathway mechanisms.

Figure 3 Preincubation of Dsh in Xenopus Egg Extracts Abolishes the Lag in Dsh Activity
Labeled β-catenin was incubated in Xenopus extracts on ice 30 min prior to (B) or 30 min after (A) the extract had been preincubated with 1 μM Dsh. No degradation of the labeled β-catenin was detected while the reactions were on ice. The reactions were started by shifting to 20°C.

Clues to Axin Activity from Its Very Low Cellular Concentration
In establishing quantities for our model in Table 1, we found that the axin concentration (20 pM) is much lower than the concentration of the other major components (β-catenin, 35 nM; APC, 100 nM; Dsh, 100 nM; and GSK3β, 50 nM). This unusual finding suggests that the function of the Wnt signaling system may actually depend on a low axin concentration. Our theoretical predictions for the effects of axin, GSK3β, and Dsh on the half-lives of β-catenin are shown in Figure 4A and 4B, respectively. At zero concentration of Dsh, doubling the concentration of axin (from the reference state, indicated as 0, to a state where the concentration has been increased by 0.02 nM) causes a 50% drop in the half-life of β-catenin. By contrast, a doubling of the GSK3β concentration only decreases the half-life of β-catenin by 10%. The small effect of GSK3β is predicted to be due to the fact that only a limited amount of axin can be recruited to the degradation complex through binding to additional GSK3β. On the other hand, increased axin concentrations are immediately translated into an increased concentration of the destruction complex, because the concentrations of APC and GSK3β are high. Changing the concentration of either GSK3β or of axin should also change the amount of Dsha required to inhibit β-catenin degradation, but the pathway is much more sensitive to axin concentration than it is to GSK3β concentration. In the presence of high concentrations of axin, the effect of Dsha should be blocked; high concentrations of axin will lead to high concentrations of the phosphorylated destruction complex no matter what level of Dsha activity is present. High levels of the destruction complex will require even higher levels of Dsh to overcome the inhibition. The interaction between Dsha and GSK3β is similar in principle: Dsh-mediated release of GSK3β (step 3) from the degradation complex can simply be reversed by sufficiently high concentrations of GSK3β (step 6). In this case, however, the effect is small. Thus, axin blocks the action of Dsh so effectively that it renders the Dsh pathway inoperable.

Figure 4 The Effect of Dsh versus Axin or GSK3β on the Half-Life of β-Catenin in Xenopus Extracts
(A and B) Predicted effects of Dsh, axin, and GSK3β on the half-life of β-catenin degradation. The half-lives are calculated from simulated degradation curves. Data are plotted as function of added Dsh (logarithmic scale) for various concentrations of axin (A) and GSK3β (B).

(C and D) Measured effects of Dsh, axin, and GSK3β on the half-life of β-catenin degradation. Stimulation of β-catenin degradation by axin occurs throughout the range of Dsh concentrations tested. (C) Axin increases the rate of β-catenin degradation even in the absence of added Dsh. (D) Stimulation of β-catenin degradation by GSK3β is detected only at high concentrations of Dsh. No effects of GSK3β on β-catenin degradation can be detected at less than 30 nM added Dsh. There is a disparity between the concentrations of axin in the experimental and theoretical curves. We assume that this is most likely due to the specific activity of the expressed axin protein.

In Figure 4C and 4D, we studied experimentally the dose-dependent effects of Dsh, GSK3β, and axin on β-catenin degradation. These curves represent β-catenin half-lives for various concentrations of axin (Figure 4C) and GSK3β (Figure 4D) with varying concentrations of Dsh. The results are qualitatively similar to those predicted by the model. As expected, β-catenin degradation is inhibited by increasing Dsh concentration and stimulated by increasing the concentration of either axin or GSK3β. There are, however, two pronounced differences in the effects of axin and GSK3β on Dsh inhibition. Whereas axin activates β-catenin degradation over a wide range of Dsh concentrations (Figure 4C), the effect of GSK3β becomes significant only at high concentrations of Dsh (Figure 4D). Furthermore, the inhibitory effect of Dsh can be almost completely blocked by high concentrations of axin (10 nM). In contrast, GSK3β (1 μM) can only partially inhibit the strong inhibitory effect of Dsh on β-catenin degradation.

Our experimental results, however, show a smaller effect on the half-life of β-catenin degradation at high concentrations of Dsh as GSK3β levels are increased. Also, the concentrations of added axin in the theoretical curve and the experimental curves are very different. The quantitative difference between the model and experimental may simply reflect the fact that the specific activity of our GSK3β and axin preparations (purified from Sf9 cells and bacteria, respectively) may be low and that a significant fraction of the recombinant proteins may not be active. Alternatively, the low activity of GSK3β may point to an unidentified inhibitory activity present in our Xenopus egg extracts.

Effects of Dynamic Changes in Protein Concentrations
The dependence of flux on the concentration of a pathway component is a measure of how much the flux is sensitively controlled by that component. In metabolic control theory, the normalized concentration-dependent parameters of the total flux known as control coefficients have been very useful in defining the characteristics of pathways (Heinrich and Rapoport 1974; Fell 1997). Similarly, in the analysis of bacterial chemotaxis, the response of a behavioral parameter as a function of changes in specific kinetic rates has been termed robustness (Alon et al. 1999). Such terms are rarely measured in signal transduction.

To determine the effects of changes in the levels of Wnt pathway components, we analyzed how the flux (β-catenin degradation) changes with changes in the concentrations of APC
0, GSK3β
0, Dsh
0, and TCF
0 (see Figure S2).

We chose to focus on the effects of changes in the concentrations of pathway components in the reference state, because similar effects were also seen for the stimulated state. Recently, we investigated a new and important property of the Wnt pathway, namely that the degradation of axin (reaction 15) is dependent on APC (unpublished data). The degradation rate of axin is mathematically expressed in the following manner:
  where KM represents a half-saturation constant for the activating effect of APC.


The theoretical effect of APC on the concentrations of both β-catenin and axin is shown in Figure 5, where we considered independently the effect of APC-mediated degradation of axin (“with regulatory loop” where Equation [5] is applied) or the absence of such an effect (where the linear rate equation ν
15 
= k
15
axin is applied). With APC-mediated axin degradation, β-catenin degradation is affected very little by changes in the concentration of APC (25% decrease with a 2-fold increase in APC concentration). This resistance to changes of β-catenin levels upon changes in APC concentration is due to the APC-dependence of axin degradation (see Figure 1 and Equation [5]). Decreasing the concentration of APC inhibits the degradation of axin, thereby promoting the formation of the degradation complex. As shown in Figure 5, in the absence of the regulatory loop, axin degradation is APC independent, homeostasis is lost, and β-catenin levels are greatly upregulated with decreasing APC concentrations. A comparison of the curves that represent the dependence and independence of axin degradation on APC (dashed lines in Figure 5) indicates that the regulatory loop acts in such a way that the normally inhibitory effect on β-catenin degradation as a result of lowering the concentration of APC is counteracted by an increase in axin levels.

Figure 5 Effect of the Regulatory Loop for Axin Degradation
The case “with regulatory loop” takes into account that axin degradation is APC-dependent (black curves). Alternatively, the case without this regulatory loop is considered (red curves). For the regulatory loop, the rate law (5) is used assuming that in the reference state the APC activation is half of its maximum (KM = 98.0 nM). The value of k′15 was chosen such that in the reference state both cases, with and without regulatory loop, yield the same degradation rate of axin (k′15 = 0.33 min−1).

We have also simulated the effects of changes in the rate of β-catenin (ν
12) and axin (ν
14) synthesis on both β-catenin and axin levels (see Figure S3). Interestingly, changing the level of axin or β-catenin affects the concentration of the other component in different ways. An increase in the synthesis of axin results in a decrease in β-catenin, whereas increasing β-catenin synthesis leads to an increase in axin levels. This latter effect contrasts with effects observed upon changes of other parameters (see Figure S2) that affect the concentrations of axin and β-catenin in opposite directions.

Transient Stimulation of the Pathway
Wnt stimulation in vivo is transient, likely due to receptor inactivation/internalization and/or other downregulatory processes.

We model transient Wnt stimulation by an exponential decay:

  where the reciprocal of λ represents the characteristic lifetime τW of receptor stimulation and t
0 denotes the onset of signaling. The concentration changes of all other pathway compounds resulting from Wnt stimulation can be calculated by numerical solution of the system equations (see Dataset S1), with initial values of the variables corresponding to the reference state.

Regulating axin turnover is important for Wnt signaling. Wnt-stimulated axin turnover has been reported in cultured mammalian cells (Yamamoto et al. 1999) and in Drosophila (Tolwinski et al. 2003). In a future paper we will show that axin turnover is affected inversely to β-catenin turnover by phosphorylation by GSK3β. Here we show theoretically that this regulated axin turnover sharply affects the dynamics of the response. Figure 6 shows the time-dependent behavior of the total concentration of β-catenin and the total concentration of axin upon transient Wnt stimulation. The concentration of β-catenin increases transiently and then returns to its initial value. In contrast, the concentration of axin is temporarily downregulated. Further analysis of Figure 6 reveals that the amplitude of the β-catenin signal upon transient stimulation is significantly lower than the steady-state concentration upon permanent stimulation (W = 1; see Figure S1). The curves a and a′ in Figure 6 are calculated for the reference values of the rate of axin synthesis and of the rate constant of axin degradation, whereas the curves b and b′ and the curves c and c′ are obtained for the case where both parameters are increased by a factor of 5 and decreased by a factor of 5, respectively. Under these conditions, both the degradation rate and the synthesis rate are altered by the same factor, thus maintaining essentially identical steady-state concentrations of axin. As a result, the steady-state concentrations of axin are the same in the unstimulated condition (W = 0) and after diminution of the Wnt signal; however, during active signaling, the differences in the dynamic nature of signal output at differing rates of axin turnover are dramatically revealed.

Figure 6 Timecourse of β-Catenin and Axin Concentrations Following a Transient Wnt Stimulation
Transient activation of the pathway is modeled assuming a Wnt stimulus that decays exponentially (Equation [6] with τW = 1/λ = 20 min) starting at t
0 = 0. The straight line for t < 0 corresponds to the steady state before pathway stimulation. The curves are obtained by numerical integration of the differential equation system (see Dataset S1). The various curves for β-catenin and for axin differ in the turnover rate of axin determined by the parameters ν
14 and k
15 (curves a: reference values of these parameters; curves b: increase by a factor of 5; curves c: reduction by a factor of 5). All other parameters are given in the legend of Table 2.

Interestingly, an increase in the turnover rate of axin leads to higher amplitudes and shorter durations of the β-catenin signal. This can be explained by the faster degradation of axin after its Dsh-mediated release from the destruction complex.Thus, β-catenin degradation is effectively inhibited for a certain time period due to a reduced availability of the scaffold axin.

Since the steady-state concentration of free axin remains unchanged (rate of axin synthesis equals the rate of its degradation) during the transition from W = 0 to W = 1, a fast axin turnover favors rapid replenishment of the axin pool after the decline of the Wnt stimulus and, in this way, fast recovery of the destruction complex. This explains why the β-catenin signal is not only amplified, but becomes more spike-like. Increasing the turnover rate of axin affects the response of axin to temporary Wnt stimulation in a similar way as the response of β-catenin; i.e., the signal is amplified and sharpened (Figure 6). Closer inspection of Figure 6 reveals that the axin response precedes the β-catenin response. For example, in the reference case, the β-catenin concentration reaches its maximum at about 260 min (curve a), whereas the minimum of the axin concentration is reached at 130 min (curve a′). This effect can be understood by observing that it is the lowering of the axin concentration that decreases the concentration of the destruction core complexes; in turn, this stabilizes β-catenin.

Mechanistic Differences between APC and Axin as Scaffolds
As the axin concentration is several orders of magnitude lower than that of the other components in the degradation pathway (see Table 1), we decided to test the effect of increasing axin levels (up to, equal to, and greater than the concentrations of other components in the pathway). To do this, we had to extend the model to include additional reactions, marked in blue in Figure 1; these had previously been neglected due to the very low axin concentrations. High axin concentrations affect most prominently the formation of the β-catenin/axin complex. Assuming a realistic value for the β-catenin–axin dissociation constant (K
18
 = 1 nM), a moderate increase in axin concentration should theoretically accelerate β-catenin degradation, whereas a much higher concentration should result in inhibition of β-catenin degradation, due to the formation of partial complexes on axin. A more extensive analysis of β-catenin half-lives over a range of axin concentrations shows such a biphasic curve (Figure 7A, curve b). These effects can also be seen experimentally in extracts (Figure 7B), where 10 nM axin accelerates and 300 nM axin inhibits β-catenin degradation. The t
½ decrease for low amounts of added axin can be easily explained by the fact that greater amounts of APC and GSK3β can be recruited to form the destruction complex. As a result, the t
½ decreases from 60 min to t
½ = 3 − 4 min. The inhibitory effect of axin becomes apparent only for axin concentrations approaching that of the other components. As shown in Figure 7A, the effect of axin binding only to GSK3β (K
19 = 1 nM, K
18 → ∞) only becomes inhibitory at higher than micromolar concentration (curve c), whereas the combined effect of binding to both β-catenin and GSK3β (K
18 = 1 nM, K
19 = 1 nM) shows inhibition at less than 500 nM (curve d). If, however, we model an ordered process of binding to axin, then abortive inhibitory complexes cannot form. We show this in Figure 7A. Here there is no separate binding of axin to β-catenin or GSK3β. In this case, there is no increase in the t½ at high axin concentrations (Figure 7A, curve a).

Figure 7 Effects of Increasing Axin Concentration on β-Catenin Degradation
(A) Effect of axin concentration on β-catenin half-life. Curve a: reference case (K
18, K
19 > 1 nM, ordered mechanism); curve b: K
18 = 1 nM, K
19 > 1 nM; curve c: K
18 > 1 nM, K
19 = 1 nM; curve d: K
18 = 1 nM.

(B) High concentration of axin inhibits β-catenin degradation in Xenopus egg extracts. Labeled β-catenin was incubated in Xenopus extracts in the absence (0 nM) or presence of moderate (10 nM) and high (300 nM) concentrations of axin. Moderate concentrations of axin greatly accelerate, whereas high concentrations inhibit β-catenin degradation.

We also examined theoretically the effects of increasing APC concentration on the half-life of β-catenin, as shown in Figure 8. The black curve corresponds to a nonordered mechanism, such as that found in axin, in which the β-catenin–APC dissociation constant (reaction 17) is low. The inhibitory effect of APC at high concentrations is due to its β-catenin buffering activity. The green curve corresponds to an ordered mechanism and reflects a high β-catenin–APC dissociation constant (high K
17). In this case, increasing concentrations of APC greater than the reference concentrations does not lead to inhibition of β-catenin degradation even at very high concentrations of APC. In cultured cells, overexpression of APC stimulates β-catenin degradation (Munemitsu et al. 1995; Papkoff et al. 1996). Unfortunately, we are presently unable to express full-length APC in Xenopus egg extracts to measure the effects of high levels in the extract system.

Figure 8 Effects of APC Concentrations on β-Catenin Degradation
Effect of APC concentration on β-catenin half-life assuming an ordered (curve a) or nonordered mechanism (curve b: K
17 = 1,200 nM), respectively.

β-Catenin can also be degraded by nonaxin-dependent mechanisms, which include Siah-1 and presenilin-mediated degradation. Though they are expected to contribute very little to the total flux through the pathway, the nonaxin-dependent processes may have very important influences under certain conditions. In our Xenopus system, these alternative pathways do not contribute greatly to the half-life of β-catenin. Experimentally, we have measured only a 1.5% contribution to total β-catenin degradation such that the half-life of β-catenin is 45 h when the axin-dependent processes are inhibited. If in some situations the nonaxin-dependent degradation contributed 10% to the flux, the half-life would be 6.3 h (k
13 = 1.83 · 10−3 min−1). The alternative pathways have very little effect on the half-life of β-catenin at normal and supranormal concentrations of APC. However, the effect of these alternative pathways becomes much more prominent when the APC concentration is lowered, a situation that may be significant under pathological conditions. As seen in Figure 9A, when APC levels are at 50% of their normal concentration, there are dramatic differences in β-catenin concentration, depending on whether the alternative degradation pathway contributes to 1.5% or 10% of the total β-catenin degradation activity. The importance of the regulatory loop involving APC-mediated axin degradation is shown in Figure 9B. In the absence of the regulatory loop, a significant inhibition of APC levels would strongly inhibit axin degradation, leading to a large increase in β-catenin levels. The control of β-catenin would be very brittle in this circumstance. However, by making axin degradation dependent on APC, a loss of APC would not stabilize axin levels, and the high axin levels would support continued degradation of β-catenin. This is the situation labeled “with regulatory loop” shown in Figure 9B. The control of axin degradation could be a decisive factor in the response of the system to genetic or environmental effects on APC.

Figure 9 Effects of the Alternative β-Catenin Degradation Pathway and of Axin Degradation at Low Concentrations of APC
(A) The alternative β-catenin degradation pathway (axin independent) can have profound effects on β-catenin levels at low APC concentrations. Variations of β-catenin and axin resulting from changes in APC concentration were calculated from the standard stimulated state. Relative variations were plotted since variation in the share of alternative degradation (1%, 5%, and 10%) results in changes of the standard stimulated state (all parameters are constant). β-Catenin and axin levels for varying contributions of the alternative degradation pathway are as follows: 1.5%, β-catenin 178 nM, axin 0.00728 nM; 5%, β-catenin 151 nM, axin 0.00679 nM; 10%, β-catenin 125 nM, axin 0.00629 nM.

(B) Inhibition of axin degradation reduces β-catenin concentration after loss of APC. Plotted is the concentration of a potential proteasome inhibitor I (scaled to its inhibition constant, K
I) necessary to reduce β-catenin concentration to its original level, depending on the concentration of APC.

Control, Modular Composition, and Robustness of the Wnt Pathway
The model contains many parameters that affect the system behavior in different ways and to various extents. We can systematically investigate these parameters and look for those whose perturbation the system is most sensitive or most robust against. We focus on the concentrations of β-catenin and axin and calculate the responses in the total concentrations of these two compounds upon changes in the rates of the individual processes. For quantifying the effects of the rate constants k+i and k−i, we use control coefficients for the total concentration of β-catenin

  and corresponding definitions for the control coefficients Caxin±i for the total axin concentration. These coefficients, originally proposed for quantifying control in metabolic networks (for reviews, see Heinrich and Schuster 1996; Fell 1997), describe the relative changes of the concentrations of the given compounds to relative changes of the rate constants. The control coefficients for the reference state are listed in Table 3. It should be remembered that the following discussion refers to small perturbations of the reference state.

Table 3 Control Coefficients for the Total Concentrations of β-Catenin and Axin and Parameters Quantifying the Sensitivity and the Robustness of the Wnt/β-Catenin Pathway
The control coefficients (Equation 7) were obtained by numerical determination of the response to a change of the rate constants of all steps by 1%. Using relative changes of rate constants less than 1% does not lead to a significant improvement of the precision of the C values. Coefficients are given for the reference state. Horizontal lines separate the coefficients for distinct modules of the pathway. The last block contains the coefficients for parameters that enter the systems equations as binding rate constants k+j and dissociation rate constants k−j via dissociation constants Kj = k−j / k+j. The upper signs of these coefficients refer to changes in k+j and the lower sign to changes in k−j. The sum of the control coefficients in each column is zero. Additional summation rules hold true for the rate constants within each module as well as for the two rate constants of each binding equilibrium. The standard deviation σ of the concentration control coefficients and the robustness ρ for β-catenin and axin are calculated by applying Equations (8) and (9)

For the reference state, there are six steps exerting strong negative control on the total β-catenin concentration (Cβcati ≅ −1). This group includes the reactions participating in assembling the destruction complex APC*/axin*/GSK3β. The corresponding parameters involve the rate constants k
7 for the binding of axin to APC, k
6 for the association of GSK3β to the APC/axin complex, and k
4 for the phosphosphorylation of axin and APC in the destruction complex. Similar strong negative control is exerted by β-catenin binding to the phosphorylated destruction complex (rate constant: k
8), the phosphorylation of β-catenin in the destruction complex (rate constant: k
9), and the synthesis of axin (ν
14).

Six other reactions exert strong positive control in the reference state on the total concentration of β-catenin (concentration (Cβcati ≅ 1). To this group belong the reactions participating in the disassembly of the destruction complex APC*/axin*/GSK3β, which are described by the rate constants k−
7 for the dissociation of the APC/axin complex, k−
6 for the dissociation of GSK3β from the destruction complex, and k
5 for the dephosphorylation of the APC and axin in the destruction complex. Other steps with a high positive control are the dissociation of β-catenin from the destruction complex (rate constant: k−
8), axin degradation (rate constant: k
15), and β-catenin synthesis (ν
12).


There are many reactions exerting almost no control on β-catenin levels in the reference state. This group includes binding of β-catenin to TCF and APC (k
16 and k
17), and the corresponding dissociation processes (k−
16 and k−
17; again only valid for small perturbations). Interestingly, the effects of the two β-catenin degradation processes (rate constants: k
11 and k
13) are also small. Calculation of control coefficients for the standard stimulated state reveals that some steps that exert no control in the reference state become important. These are the activation and inactivation of Dsh (rate constants: k
1 and k
2) and, more pronounced, the Dsh-mediated release of GSK3β from the destruction complex (k
3). For all other processes, the signs of the control coefficients for β-catenin and axin do not change at the transition from the reference state to the standard stimulated state. The effects of parameter changes on axin are generally opposite to those on β-catenin; i.e., processes with a positive control coefficient for β-catenin have negative control coefficients for axin and vice versa. A significant exception is the synthesis of β-catenin, which exerts a positive control not only on β-catenin but also on axin, as expected from the results obtained in the last section.

Closer inspection of Table 3 reveals that the values of the control coefficients for the rate constants sum up to zero. This fact is known as the summation theorem for concentration control (Heinrich and Rapoport 1974) and is valid for all reaction networks at steady state. This result finds its explanation in the invariance of the steady-state concentrations against simultaneous change of all rate constants by the same factor. Interestingly, in the present case there are subgroups of processes whose control coefficients separately sum up to zero, indicating a modular structure of the pathway. In Table 3, the control coefficients of the different modules are separated by horizontal lines. The main four subgroups are the Dsh module (not shown in Table 3), the kinase/phosphatase module, the β-catenin module, and the axin module. A subgroup is defined by a set of reactions where the control coefficients of the binding reactions are opposite to those of the corresponding dissociation reactions (C+i = −C−i for i = 6, 7, 8, 16, 17).

For those more familiar with genetic manipulation, it is more common to vary the concentrations of individual components rather than vary the rate constant of a reaction. Table 4 shows the control coefficients for β-catenin and axin calculated for changes in the total concentrations of pathway components instead of the rate constants. Using the values of Table 4, the potential tumor-supressing effects (of APC, GSK3β, and axin) and potential oncogenic effects (of PP2A, TCF, Dsh, β-catenin) can be explained and quantified. It may be worth mentioning that there is no summation theorem for the control coefficients when calculated by changing total concentrations instead of rate constants. For practical reasons, it may be easier to discuss the coefficients with respect to concentration changes (Table 4); for theoretical reasons, changing rate constants are simpler to handle. We think that eventually it will also be clearest to speak about oncogenic reactions instead of oncogenic genes, especially if we are thinking of oncogenesis in response to pharmacologic or environmental perturbations. Genetic defects then can be considered in terms of changes in activity, transcription, translation, or proteolysis.

Table 4 Concentration Control Coefficients for the Total Concentrations of β-Catenin and Axin Relative to Changes in the Concentrations of Pathway Components
The control coefficients were obtained by numerical determination of the response to a change of total concentrations by 1%. Coefficients are given for the reference state and for the standard stimulated state

Clearly, the robustness of a variable towards parameter changes is higher the lower the corresponding concentration control coefficient. To arrive at an estimation of the overall effects of parameter perturbations on the system as a whole, we consider first the standard deviation σ of the control coefficients from their mean value. According to the summation theorem, the mean value of all control coefficients for a given variable is zero. Thus, we get for the standard deviation for the control coefficients of β-catenin:
  where the summation is performed over all reactions, including forward and backward steps of fast equilibria. High values of σ indicate that the given variable is on average very sensitive towards changes of rate constants. We propose to introduce a measure for the robustness ρ of a variable towards changes of all parameters in the following way:
  


As σ may vary between zero and infinity, the range of ρ is confined to the interval 1≥ ρ ≥ 0. High values of ρ resulting from low σ values for the control coefficients indicate that the variable is robust against parameter perturbations. The standard deviations σ of the control coefficients and the ρ values for β-catenin and axin are presented in the last two rows of Table 3. Because many control coefficients are close to zero and the absolute values of the others hardly exceed unity, the σ values for β-catenin as well as for axin are rather small. Since all values for σ are lower than unity, a 1% change in a rate constant leads, on average, to a response of <1% in the overall level of β-catenin. The total concentration of axin is more robust against parameter perturbations than the total concentration of β-catenin, particularly in the standard stimulated state. A transition from the reference to the standard stimulated state results in a lower robustness for β-catenin and a higher robustness for axin.

Discussion
Theory and quantitation are mutually dependent activities. It would seem unlikely that one would go to the trouble to measure detailed kinetic quantities without a specific model to test, and it is equally unlikely that realistic models can be constructed without the constraints of quantitative experimental data. Our intent in trying to reproduce a substantial part of the Wnt pathway in Xenopus egg extracts was to acquire the kind of detailed kinetic data required to build a realistic model. There are several unusual advantages to the extract system that contributed to this effort. The Xenopus egg extract is essentially neat cytoplasm; it reproduces the in vivo rate of β-catenin degradation and responds to known regulators as expected from in vivo experiments. Kinetic experiments with high time resolution are possible in this system, since a well-stirred extract is presumably synchronous in ways in which collections of cells may not be. In extracts it is possible to precisely set the level of components by depletion or addition. The direct output of the canonical Wnt pathway is an easily measured cytoplasmic event, the degradation of β-catenin. Thus, in this unusual system it is possible to acquire quantitative information about signaling pathways, not achievable in vivo. At the same time, these extracts have limitations. We have not considered the receptor events, and it is likely that reactions at the plasma membrane contribute to dynamic features. Also, our analysis is incomplete, as there are other components of Wnt signaling, such as casein kinase Iδ, casein kinase Iɛ, and PAR1, as well as cross-talk from other pathways, that influence the behavior of the system. We have also oversimplified the multiple phosphorylation steps. We have assumed a simple interconversion of the phosphorylated and unphosphorylated complex of axin, APC, and GSK3β, whereas in reality multiple phosphorylation states exist within the complex; the states may be random or sequential. We simply do not have the information to provide a much more specific model of phosphorylation interconversions at this time, although the model could easily be extended. Finally, there is the question of what Wnt process we are studying. We are looking at events in the cytoplasm of unfertilized eggs. Though endowed with all of the core components of the Wnt pathway, the egg is, as far as we know, transcriptionally silent and not involved in Wnt signaling, though this system is active very soon in embryogenesis. Thus, there is no biological in vivo behavior with which to compare the in vitro behavior. Nevertheless, the basic core circuitry is intact and is presumably prepared for the early Wnt events in the embryo. All the properties of the egg extract system are very similar to that circuitry in vertebrate somatic cells.

To build a mathematical description of the Wnt signaling system, we started with the basic circuitry discerned from previous studies in Xenopus embryos and mammalian cells, whose similarity to the in vitro system we had already confirmed. We derived a system of differential equations that described the time-dependent variations of the system variables, i.e., the concentrations of the pathway components and their complexes. Parameters of the model are binding constants of proteins, rate constants of phosphorylations and dephosphorylations, rate constants of protein degradation, and rates of protein synthesis. Model reduction was achieved by considering conservation relations and by applying rapid equilibrium approximations for selected binding processes. Despite these simplifications, the model consists of a nonlinear system of differential equations whose solution requires the use of computers. Not all of these parameters were accessible to measurement. To circumvent this problem, we used as primary inputs not only kinetic parameters characterizing individual steps, but quantities that are more easily accessible from experiment, such as the overall flux of β-catenin degradation. This allowed us to derive rate constants as well as protein concentrations in a reference state, where there was no Wnt signal. This state serves as a starting point for predicting the system behavior during Wnt signaling as well as after experimental perturbations.

The basic model reproduced quantitatively the behavior of the reference state, including perturbations of this state achieved by varying the concentration of axin, GSK3β, and TCF. It also reproduced extensions of this to the signaling state. A wide variety of different sets of experimental data could be simulated by the same model, employing the same sets of kinetic parameters. We approached this process iteratively. For example, the early model did not include nonaxin-dependent degradation of β-catenin, but inclusion of this process improved the fit to the experimental data. More significantly, addition of this process had interesting biological implications, which we discuss.

In many ways, one of the most peculiar findings was the very low concentration of axin in the Xenopus extracts. Axin levels in other organisms may similarly be very low: Drosophila axin can be detected by Western blotting only following its immunoprecipitation (Willert et al. 1999). Although our theoretical and experimental studies have shown that axin is inhibitory at high concentrations, both indicate that axin is not present at the optimal concentration for the highest rate of β-catenin degradation. Therefore, axin levels are not set for optimality of β-catenin degradation, but are presumably optimized for some other purpose. Theoretically, axin levels must be held below the very sharp threshold of Dsh inhibition. Experimentally, these thresholds, which blunt Wnt signaling, are observed but are not as sharp as expected, and this may indicate some other compensatory effects. These thresholds would limit axin concentration to well below 1 nM if activated Dsh were constrained to concentrations of below 1 μM. Under these circumstances, we can expect that axin would never be found at concentrations approaching those of other Wnt pathway components (50–100 nM).

The low concentration of axin relative to other components (such as GSK3β, Dsh, and APC) has another design feature potentially very general and important for the modularity of metazoan signaling pathways. Axin is a critical node point for controlling β-catenin levels, but it also interacts with components shared with several other important pathways. The interaction of these components with axin fluctuates due to Wnt signals (reflecting changes in binding as well as changes in axin levels), yet because the concentration of axin is so low, there will be no appreciable change in the overall levels of GSK3β, Dsh, or APC (all these components important in other pathways would otherwise be driven to fluctuate). The very low axin concentration thus isolates the Wnt pathway from perturbing other systems, a simple mechanism to achieve modularity. Other scaffold proteins may serve similar functions in other pathways. These insights follow from a very simple measurement of axin concentration and suggest the utility of measuring the levels of signaling pathway components in different cell types and circumstances. Since quantitative and kinetic features may be important in defining modules, it suggests that qualitative circuit diagrams of signal transduction may overlook very important design features. Modularity within the Wnt pathway can be defined by an extension of the summation theorem of Heinrich and Rapoport (1974), which argues that the steady state of an entire pathway would have control coefficients that added to zero. When the Wnt pathway is broken down to several subpathways, we find that within these subpathways the control coefficients would sum to zero at steady state. While some of this subdivision is obvious (i.e., the kinase phosphatase module involving the phosporylation of APC and axin complexed to GSK3β), in other cases, such as the β-catenin module, it is much less obvious. Here the reactions include the phosphorylation of β-catenin in the APC/axin/GSK3β complex, the release and degradation of β-catenin, and the synthesis and nonaxin-dependent degradation of β-catenin. Balanced perturbation of these subpathways as a whole will not affect the overall flux of β-catenin degradation. It is not clear whether this concept of modularity might be extended usefully in two other directions: modularity in systems not at steady state, i.e., with transients, and estimates of linkage between pathways by some definition of nonzero summations expressing the degree of independence or modularity.

In addition to work by Kholodenko et al. (1997), this paper marks one of the first extensions of metabolic control theory to signal transduction. Metabolism and signal transduction seem very different, the former involving the transfer of mass and the latter the transfer of information. In addition, metabolic pathways generally involve dedicated components and the specificity of interaction of substrates and enzymes is very high. Signaling pathways share many components; interactions are often weak. Metabolism, which has had a long history of quantitative study, was a natural field for the development of control theory, and this theory has been successful in converting the specific information about the behavior of enzymes in a pathway to the overall behavior of metabolic circuits. Control coefficients are useful measures of the impact of a process or quantity on another. In its application to metabolism, it allowed us to dispose of erroneous concepts, such as the notion of a rate-determining step. In signal transduction, control coefficients might play a similar role. Here they can be used to indicate quantitively the effects of a particular reaction on some other property, such as flux through the pathway or concentration of another component. By this definition, certain rate constants, such as the phosphorylation and dephosphorylation of APC and axin, have a major influence on the levels of β-catenin, while others, such as the degradation rate of phosphorylated β-catenin, have little effect. The sign and magnitude of these control coefficients give some indication what gene products could be oncogenes or tumor suppressors. As shown in Table 4, by this criterion APC, GSK3β, and axin are potent tumor suppressors, whereas β-catenin is an oncogene. Dsh would be expected to exert only moderate oncogenic effects. Clearly the effects of certain gene products are dependent on context, including their rate of synthesis and steady-state concentration. As our understanding of pathways improve, the effect of mutation or pharmacologic inhibition could be estimated quantitatively using control coefficients. The differences between cell types and organisms could be exploited to better predict mutagenic and pharmacologic impact on signal propagation.

Despite considerable progress in identifying components of the Wnt pathway, many important mechanistic details are still lacking. In this analysis we have shown that Dsh seems to act to prevent the phosphorylation of the axin/APC complex, not the phosphorylation of β-catenin. Dsh (complexed to GBP) does not seem to be a general GSK3β inhibitor, like Li+, but rather is focused on the two scaffolding proteins. This was apparent from the biphasic nature of both the theoretical and experimental curves, which suggested that Dsh inhibited the rephosphorylation of axin/APC, but still allowed many cycles of β-catenin phosphorylation, ubiquitination, and degradation. This mechanism was further proven by a timing-of-addition experiment. It needs to be further confirmed and extended by looking specifically at individual phosphorylation sites on all the components of the complex. Another insight into the mechanisms of complex formation and control of β-catenin degradation concerns the inhibition of β-catenin degradation at concentrations of axin approaching those of other components. This suggests that axin binds APC, GSK3β, and β-catenin in random order. As discussed above, the axin concentration is limited by other factors; owing to the low concentration of axin, random binding is not likely ever to be a problem. The situation for APC seems very different. The concentration of APC is comparable to that of the other components. Overexpression studies show no inhibitory effects. These theoretical and experimental observations suggest that APC as a scaffold must be very different from axin as a scaffold. Most likely, APC binds components in an ordered manner.

Metabolic pathways are understandable in terms of the familiar logic of chemical synthesis; signal transduction pathways, by contrast, often do not seem to conform to simple design principles. It is not clear at all whether signaling pathways have been optimized for a specific function or instead whether they are remnants of some early and rather arbitrary evolutionary experiment, now embedded in other processes that are difficult to change. Systems analysis, along with experiment, offers some hope of uncovering latent principles of design. For example, the modeling of the Wnt pathway gave a theoretical insight into the function of axin degradation in Wnt signaling. The degree of axin instability dramatically affects the amplitude and duration of the β-catenin response to a transient Wnt signal. If axin turnover were designed to be slow, then β-catenin would rise slowly to a low amplitude and persist for many hours. In a system where axin turnover was more rapid, the amplitude could increase several-fold and would persist a shorter time. The duration and amplitude of the response are likely to be important factors in developmental systems, which may respond differently to different amplitudes and durations of a signal. In addition, some developmental processes occur with such rapidity that the same signal would be interpreted differently at different times, hence the need to quickly terminate a signal. The very different effects of transient and persistent signals in the same pathway have been studied in PC12 cells in the MAP kinase pathway activated by EGF or NGF (Marshall 1995). Finally, APC-dependent axin degradation stabilizes the Wnt pathway to variations in the APC concentration. Viewed from this perspective, the regulatory loop involving APC and axin degradation is an important design feature of the Wnt pathway.

Robustness has also been considered an important design principle for signaling processes (Alon et al. 1999), and control coefficients can be a good measure of this robustness. We present here a general measure of robustness of the entire pathway, using a measure that sums the variation in every individual reaction. Though it is generally thought that “robust” is good, the complement of robust is adaptability, and it may be that some aspects of a signaling pathway are designed to be responsive to changes in some parameters so that the same pathway can be used differently in different circumstances by altering key parameters. Since quantitative measures of the concentration or posttranslational modification of signaling proteins are rare in the literature, we have very little information on whether the organism varies certain key components to achieve different behavior of the signaling systems.

Another aspect of robustness is susceptibility to mutation or pharmacologic or environmental perturbation. The unexpected minimal phenotypes observed in numerous mouse knockout experiments have underscored our ignorance of the adaptable responses of organisms and in particular the adaptable nature of signaling pathways. One unexpected theoretical observation in this paper was the potential importance of the nonaxin-dependent degradation for β-catenin, under conditions where the APC levels are reduced. In our model, the nonaxin-dependent degradation contributed only a few percent to the overall flux of β-catenin degradation. Yet if the APC levels fall only 50%, the exact level of the alternative pathway made a large difference in the steady-state level of β-catenin. If the activity of the alternative pathways varied in different tissues, then this simple but largely silent effect could explain the tissue specificity of APC mutations. Similarly, variations in the alternative pathway might also explain some aspect of individual risk to loss of a single copy of the APC gene.

An experiment can better be judged by how many questions it raises than by how many it answers. The same may be said about theoretical analysis. Such analysis is always a work in progress, in that the experimental basis is continually changing to some degree. Some of the experimental changes, though significant mechanistically, may have little effect on the model and its interpretation. Some may require major revision. In the case of the Wnt pathway, the theoretical analysis and modeling have already raised several interesting questions of biological importance. They have already stimulated further experimentation. More than anything, the modeling has increased the urgency for obtaining accurate quantitative information about both steady-state and transient processes in Wnt signaling and for obtaining information about the differences in parameters in different tissues and in different organisms.

Materials and Methods

Egg extracts and degradation assays.

Xenopus egg extracts were prepared as described previously (Salic et al. 2000). Extracts were used either used immediately or stored at –80°C after being snap-frozen in liquid nitrogen. β-Catenin degradation assays were performed as described before (Salic et al. 2000).

Measurement of β-catenin synthesis.
Freshly prepared Xenopus egg extracts were either supplemented with 25 mM LiCl in Xenopus buffer (XB) or XB and an aliquot were withdrawn for β-catenin degradation assays. The free methionine pool in Xenopus embryos is approximately 90 μM, and based on this number, [35S]methionine was added to the extract to a give a final activity of 1,000 counts per picomole methionine. Extracts were incubated at 20°C, and aliquots were withdrawn at the indicated times for SDS-PAGE, trichloroacetic acid (TCA) precipitation, and β-catenin pull-downs. To assay protein synthesis in the extract, total methionine incorporation was measured by TCA precipitation. In brief, Xenopus extracts (2 μl), metabolically labeled with [35S]methionine as above, were diluted to 100 μl with PBS and supplemented with 2 μl of 2% deoxycholate and TCA to 5%. The reaction was pelleted at 20,000 × g for 10 min at 4°C. After washing with ice-cold acetone and air drying, the radioactivity of the pellet was measured in a scintillation counter.

To isolate metabolically labeled β-catenin from Xenopus extracts, we used His-tagged APCm3 cross-linked to Ultralink beads (Pierce, Woburn, Massachusetts, United States). Since phosphorylated APC has a much higher affinity for β-catenin, APCm3 beads were first phosphorylated with 300 nM His-tagged GSK3β in 25 mM HEPES (pH 7.7), 1 mM EDTA, 300 mM NaCl, 10 mM MgCl2, 1 mM DTT, and 1 mM ATP for 1 h at room temperature with shaking. The beads were washed three times with 25 mM HEPES (pH 7.7), 1 mM EDTA, 300 mM NaCl, 1% Tween, and 1 mM DTT and were then used to pull down β-catenin. Extracts (50 μl) labeled with [35S]methionine (see above) were diluted 5× with XB containing 1% Tween and protease inhibitors. The diluted extracts were incubated with phosphorylated APCm3 beads (20 μl) at 4°C for 2 h. The beads were washed and bound protein was eluted by boiling in SDS-PAGE loading buffer. Labeled β-catenin was detected following SDS-PAGE and autoradiography.

Measuring dissociation rates of phosphorylated/nonphosphorylated β-catenin from axin.
Radiolabeled β-catenin (5 μl) was phosphorylated using 300 nM His-tagged GSK3β and 100 nM maltose-binding protein (MBP)–axin in 20 μl of XB containing 10 mM ATP, 20 mM MgSO4, and 50 mM NaCl. For the nonphorphorylated control, β-catenin was incubated as above, except that 50 mM LiCl was used instead of NaCl to inhibit GSK3β. The kinase reactions were incubated in a shaker for 30 min at 20°C and then added to 50 μl of MBP–axin, bound to amylose beads (1 mg of protein per milliliter of beads), and brought up to 250 μl with XB containing 50 mM LiCl. After phorsphorylated and nonphosphorylated β-catenin, respectively, bound to axin beads, the beads were washed three times with 500 μl of XB containing 50 mM LiCl. Dissociation of the bound β-catenin was initiated by adding 1 μM unlabeled recombinant β-catenin (His-tagged, from Sf9 cells) and incubated at 20°C in a shaker. At the appropriate times, 5 μl aliquots of beads were quickly removed, filtered through Wizard minicolumns (Promega, Madison, Wisconsin, United States), and washed with ice-cold XB (3 ml). Proteins bound to beads were eluted from the minicolumns with 20 μl of hot sample buffer, followed by SDS-PAGE and autoradiography.

Recombinant proteins.
The expression and purification of all recombinant proteins have been previously described (Salic et al. 2000). Dsh was expressed as an MBP fusion in bacteria. His-tagged GSK3β, His-tagged Tcf3, His-tagged APCm3, and MBP–axin were expressed in Sf9 cells.

Supporting Information
Dataset S1 The Roles of APC and Axin Derived from Experimental and Theoretical Analysis of the Wnt Pathway
(287 KB DOC).

Click here for additional data file.

 Figure S1 Effect of Wnt Stimulation on the Concentrations of β-Catenin and Axin
The curves represent steady-state concentrations of β-catenin (solid lines) and axin (broken lines) as functions of the strength W of Wnt stimulation. Curve a: free unphosphorylated β-catenin; curve b: free phosphorylated β-catenin; curve c: total β-catenin; curve d: total axin. All concentrations are scaled with respect to their values in the reference state. It is worth mentioning that in the model “without regulatory loop,” the steady-state concentration of free axin is determined by the condition X
12
 =
ν
14
/k
15, and is, therefore, independent of Wnt stimulation.

(2,954 KB TIFF).

Click here for additional data file.

 Figure S2 Effects of the Amounts of Pathway Components on the Concentrations of β-Catenin and Axin
This figure gives additional information with respect to the effects of Dsh, TCF, and GSK3β on the steady-state concentrations of total β-catenin (solid lines) and total axin (dashed lines) for the case of permanent Wnt-stimulation, W = 1. All concentrations and synthesis rates are scaled with respect to their values in the stimulated stationary state.

(3,472 KB TIFF).

Click here for additional data file.

 Figure S3 Effects of Synthesis Rates on the Concentrations of β-catenin and Axin
The curves represent steady-state values of total concentrations of β-catenin (solid lines) and axin (dashed lines), depending on the rates of synthesis of β-catenin and axin. All concentrations and synthesis rates are scaled with respect to their values in the stimulated stationary state.

(3,483 KB TIFF).

Click here for additional data file.

 Table S1 Mathematical Notation for Model Variables as Subdivided into Independent and Dependent Variables
(45 KB DOC).

Click here for additional data file.

 Table S2 Complete List of Model Parameters of the Wnt Signal Transduction Model
The rate constants marked with “#” play a role only in stimulated states where W ≠ 0. Note that some of the numerical values are given in a higher precision compared to Table 1.

(111 KB DOC).

Click here for additional data file.

 We thank Tom Rapoport, Rebecca Ward, and Yinon Ben-Neriah for thoughtful suggestions on the work. We thank the National Institute of Child Health and Development (grant HD037277 to MWK) for support and the National Institute of General Medical Sciences and the Harvard-Armenise Foundation for supplemental support (for RH). RH is also supported by the German Research Foundation (grant He 2049/2-1). EL is a Special Fellow of the Leukemia and Lymphoma Society. AS is supported by a Damon-Runyon Cancer Fund postdoctoral fellowship. RK is supported by the German Research Foundation (SFB 555).


Conflicts of Interest. The authors have declared that no conflicts of interest exist.


Author Contributions. EL, AS, RK, RH, and MWK conceived and designed the experiments. EL, AS, RK, and RH performed the experiments. EL, AS, RK, RH, and MWK analyzed the data. EL, AS, RK, RH, and MWK contributed reagents/materials/analysis tools. EL, AS, RK, RH, and MWK wrote the paper.

Academic Editor: Roel Nusse, Stanford University School of Medicine.

Abbreviations
APCadenomatous polyposis coli

DshDishevelled

EDTAethylene diamine tetraacetic acid

GBPglycogen synthase kinase-binding protein

GSK3βglycogen synthase kinase 3β

MBPmaltose-binding protein

PP2Aprotein phosphatase 2A

Sf9
Spodoptera frugiperda


TCAtrichloroacetic acid

TCFT-cell factor

XB
Xenopus buffer.
==== Refs
References
Alon U  Surette MG  Barkai N  Leibler S   Robustness in bacterial chemotaxis Nature 1999 397 168 171 9923680 
Dajani R  Fraser E  Roe SM  Yeo M  Good VM    Structural basis for recruitment of glycogen synthase kinase 3β to the axin–APC scaffold complex EMBO J 2003 22 494 501 12554650 
Fell D   Understanding the control of metabolism 1997 London Portland Press 300 
Gerhart J   1998 Warkany lecture: Signaling pathways in development Teratology 1999 60 226 239 10508976 
Gerhart J  Kirschner MW   Cells, embryos, and evolution 1997 Oxford Blackwell Science 642 
Heinrich R  Rapoport TA   A linear steady-state treatment of enzymatic chains: General properties, control and effector strength Eur J Biochem 1974 42 89 95 4830198 
Heinrich R  Schuster S   The regulation of cellular systems 1996 New York Chapman and Hall 372 
Heinrich R  Neel BG  Rapoport TA   Mathematical models of protein kinase signal transduction Mol Cell 2002 9 957 970 12049733 
Kang DE  Soriano S  Xia X  Eberhart CG  De Strooper B    Presenilin couples the paired phosphorylation of β-catenin independent of axin: Implications for β-catenin activation in tumorigenesis Cell 2002 110 751 762 12297048 
Kholodenko BN  Hoeck JB  Westerhoff HV  Brown GC   Quantification of information transfer via signal transduction pathways FEBS Lett 1997 414 430 434 9315734 
Lee E  Salic A  Kirschner MW   Physiological regulation of β-catenin stability by Tcf3 and CK1ɛ J Cell Biol 2001 154 983 993 11524435 
Liu J  Stevens J  Rote CA  Yost HJ  Hu Y    Siah-1 mediates a novel β-catenin degradation pathway linking p53 to the adenomatous polyposis coli protein Mol Cell 2001 7 927 936 11389840 
Marshall CJ   Specificity of receptor tyrosine kinase signaling: Transient versus sustained extracellular signal-regulated kinase activation Cell 1995 80 179 185 7834738 
Matsuzawa SI  Reed JC   Siah-1, SIP, and Ebi collaborate in a novel pathway for β-catenin degradation linked to p53 responses Mol Cell 2001 7 915 926 11389839 
Munemitsu S  Albert I  Souza B  Rubinfeld B  Polakis P   Regulation of intracellular β-catenin levels by the adenomatous polyposis coli (APC) tumor-suppressor protein Proc Natl Acad Sci U S A 1995 92 3046 3050 7708772 
Papkoff J  Rubinfeld B  Schryver B  Polakis P   Wnt-1 regulates free pools of catenins and stabilizes APC–catenin complexes Mol Cell Biol 1996 16 2128 2134 8628279 
Salic A  Lee E  Kirschner MW   Control of β-catenin stability: Reconstitution of the cytoplasmic steps of the Wnt pathway in Xenopus  egg extracts Mol Cell 2000 5 523 532 10882137 
Tolwinski NS  Wehrli M  Rives A  Erdeniz N  DiNardo S    Wg/Wnt signal can be transmitted through arrow/LRP5,6 and Axin independently of Zw3/GSK3β activity Dev Cell 2003 4 407 418 12636921 
Willert K  Logan CY  Arora A  Fish M  Nusse R   A Drosophila  Axin homolog, Daxin inhibits Wnt signaling Development 1999 126 4165 4173 10457025 
Yamamoto H  Kishida S  Kishida M  Ikeda S  Takada S    Phosphorylation of axin, a Wnt signal negative regulator, by glycogen synthase kinase-3β regulates its stability J Biol Chem 1999 274 10681 10684 10196136

PMID: 14551910
Accession ID: PMC212692
License: CC BY
Last Updated: 2021-01-05 08:21:04
Retracted: no
Citation: PLoS Biol. 2003 Oct 13; 1(1):e12
==== Front
PLoS BiolPLoS BiolpbioplosbiolPLoS Biology1544-91731545-7885Public Library of Science San Francisco, USA 10.1371/journal.pbio.0000012Research ArticleDevelopmentGenetics/Genomics/Gene TherapyMolecular Biology/Structural BiologyCaenorhabditisGenome-Wide RNAi of C. elegans Using the Hypersensitive rrf-3 Strain Reveals Novel Gene Functions Genome-Wide RNAi Screen Using rrf-3Simmer Femke 
1
Moorman Celine 
1
van der Linden Alexander M 
1
Kuijk Ewart 
1
van den Berghe Peter V.E 
1
Kamath Ravi S 
2
Fraser Andrew G 
2
Ahringer Julie 
2
Plasterk Ronald H. A plasterk@niob.knaw.nl
1
1Hubrecht Laboratory, Centre for Biomedical GeneticsUtrechtThe Netherlands2University of Cambridge, Wellcome Trust/Cancer Research Institute and Department of GeneticsCambridgeUnited Kingdom10 2003 13 10 2003 13 10 2003 1 1 e1211 6 2003 1 8 2003 Copyright: © 2003 Simmer et al.2003This is an open-access article distributed under the terms of the Creative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are properly credited.
Supersensitive Worms Reveal New Gene Functions 
RNA-mediated interference (RNAi) is a method to inhibit gene function by introduction of double-stranded RNA (dsRNA). Recently, an RNAi library was constructed that consists of bacterial clones expressing dsRNA, corresponding to nearly 90% of the 19,427 predicted genes of C. elegans. Feeding of this RNAi library to the standard wild-type laboratory strain Bristol N2 detected phenotypes for approximately 10% of the corresponding genes. To increase the number of genes for which a loss-of-function phenotype can be detected, we undertook a genome-wide RNAi screen using the rrf-3 mutant strain, which we found to be hypersensitive to RNAi. Feeding of the RNAi library to rrf-3 mutants resulted in additional loss-of-function phenotypes for 393 genes, increasing the number of genes with a phenotype by 23%. These additional phenotypes are distributed over different phenotypic classes. We also studied interexperimental variability in RNAi results and found persistent levels of false negatives. In addition, we used the RNAi phenotypes obtained with the genome-wide screens to systematically clone seven existing genetic mutants with visible phenotypes. The genome-wide RNAi screen using rrf-3 significantly increased the functional data on the C. elegans genome. The resulting dataset will be valuable in conjunction with other functional genomics approaches, as well as in other model organisms.

The screen suggested functions for 393 genes for which no RNAi-mediated phenotype was known. The comparison with similar screens in worms has general implications for RNAi experiments
==== Body
Introduction
RNA interference (RNAi) is targeted gene silencing via double-stranded RNA (dsRNA); a gene is inactivated by specific breakdown of the mRNA (Fire et al. 1998; Montgomery et al. 1998). It is an ideal method for rapid identification of in vivo gene function. Initial studies on RNAi used microinjection to deliver dsRNA (Fire et al. 1998), but it was subsequently shown that dsRNA can be introduced very easily by feeding worms with bacteria that express dsRNA (Timmons and Fire 1998). Using this technique on a global scale, an RNAi feeding library consisting of 16,757 bacterial clones that correspond to 87% of the predicted genes in Caenorhabditis elegans was constructed (Fraser et al. 2000; Kamath et al. 2003). Upon feeding to worms, these clones will give transient loss-of-function phenotypes for many genes by inactivating the target genes via RNAi. By feeding the clones in this library to wild-type Bristol N2 worms, loss-of-function phenotypes were assigned to about 10% of genes. However, RNAi phenotypes were missed for about 30% of essential genes and 60% of genes required for postembryonic development, probably because RNAi is not completely effective (Kamath et al. 2003). Other global RNAi screens have been recently performed in C. elegans using this RNAi library or other techniques (Gönczy et al. 2000; Maeda et al. 2001; Dillin et al. 2002; Piano et al. 2002; Ashrafi et al. 2003; Lee et al. 2003; Pothof et al. 2003). These screens were done using wild-type worms.

We have already shown that mutation of rrf-3, a putative RNA-directed RNA polymerase (RdRP), resulted in increased sensitivity to RNAi (Sijen et al. 2001; Simmer et al. 2002). There are four RdRP-like genes in C. elegans. Two of these, ego-1 and rrf-1, are required for efficient RNAi, as apparent from the fact that these mutants are resistant to RNAi against germline or somatically expressed genes, respectively (Smardon et al. 2000; Sijen et al. 2001). A third gene, rrf-2, appears to have no role in RNAi. The rrf-3 strain, mutated in the fourth RdRP homolog, shows an opposite response to dsRNA; this mutant has increased sensitivity to RNAi (Sijen et al. 2001).

A more detailed study of RNAi sensitivity of rrf-3 mutants using a set of 80 genes showed that rrf-3 is generally more sensitive to RNAi than wild-type worms (Simmer et al. 2002). RNAi phenotypes in rrf-3 animals are often stronger, and they more closely approximate a null phenotype, when compared to wild-type. In addition, loss-of-function RNAi phenotypes were detected for a number of genes using rrf-3 that were missed in a wild-type background. For example, known phenotypes were detected for many more neuronally expressed genes in the rrf-3 background. These features suggest that the rrf-3 strain could be used to improve and extend functional information associated with C. elegans genes.

We have conducted a genome-wide RNAi screen using the rrf-3 strain. In total, we found reproducible RNAi phenotypes for 423 clones that previously did not induce a phenotype (corresponding to 393 additional genes). To explore the variability of global RNAi screens, we performed the rrf-3 screen twice for Chromosome I and carried out a Chromosome I screen with wild-type. These were cross-compared and also compared to the results of the wild-type screen of Fraser et al. (2000). From this, we find that rrf-3 consistently allowed detection of more phenotypes than wild-type. In addition, we found that there is a significant screen-to-screenvariability (10%–30%).

Results
Comparative Analysis of RNAi for Chromosome I with Wild-Type and rrf-3

We first conducted a pilot screen of Chromosome I using rrf-3 and found RNAi phenotypes for 456 bacterial clones. We compared these data to those obtained by Fraser et al. (2000) for a screen in the wild-type Bristol N2 strain. For 153 of these 456 clones, no phenotypes were reported by Fraser et al. (2000) and phenotypes were observed for 303 clones in both screens. The N2 screen done by Fraser et al. (2000) resulted in RNAi phenotypes for 40 clones for which no phenotypes were found using rrf-3 (Figure 1A). These results indicate that rrf-3 can be used in a global screen to identify loss-of-function phenotypes for additional genes. However, some phenotypes were missed in the rrf-3 screen. To explore the reproducibility and variability of RNAi screens, we next screened the clones of Chromosome I using N2 and rrf-3 side by side. We detected phenotypes for 447 clones: 140 were found only in rrf-3, 11 only in N2, and 296 in both strains (Figure 1B). These data confirm that rrf-3 is more sensitive to RNAi and, in addition, these data indicate that global RNAi screens with rrf-3 will result in more clones with a detectable phenotype.

Figure 1 Comparison of Different RNAi Experiments of Chromosome I Using Wild-Type Bristol N2 and rrf-3

Differences between different laboratories or investigators and between experiments done within the same laboratory and by the same investigators are observed. Ovals represent the amount of bacterial clones that gave an RNAi phenotype in an experiment. Areas that overlap represent clones for which in both experiments an RNAi phenotype was detected. Differences and overlap between an RNAi experiment done with the rrf-3 mutant strain and the data obtained by Fraser et al. (2000) done with the standard laboratory strain, Bristol N2 (A); N2 and rrf-3 tested at the same time within our laboratory (B); experiments done with N2 in two different laboratories: this study (‘NL') and Fraser et al. (2000) (C); two experiments done with the same strain, rrf-3, within our laboratory (D).

Variability of the RNAi Effect
When we compared the RNAi results that we obtained using N2 with the Fraser et al. (2000) data, we were surprised to find significant differences: we only detected phenotypes for 75% of the clones that gave a phenotype in Fraser et al. (2000), and these researchers reported phenotypes for 84% of clones for which we found a phenotype (Figure 1C). The differences do not appear to be due to false positives. For example, Fraser et al. (2000) detected the predicted phenotype for goa-1 and unc-73, whereas we did not detect a mutant phenotype. Similarly, we detected the known mutant phenotype for egl-30 and cdc-25.1, which were not detected by Fraser et al. (2000). In addition, we found that the false-positive rate is negligible (see below).

It is possible that different laboratories or investigators have slightly different results. However, when we compare the results that we obtained with two independent screens of Chromosome I using rrf-3 in our laboratory, we also see differences. For 394 clones we detected a phenotype in both experiments, 54 are specific for the first experiment, and 34 for the second (Figure 1D). Among the clones that only gave an RNAi phenotype in one of the experiments are again clones that induced the predicted phenotype based on the phenotypes of genetic mutants (unc-40, gpc-2, and sur-2). These data show that large-scale RNAi screens done within the same laboratory and by the same investigators also give variable results. A few examples of variable RNAi results are shown in Table 1.

Table 1 Variable RNAi Effects
Selection of clones that induced variable RNAi results in this study (‘NL') and or in the study by Fraser et al. (2000). In this subset of bacterial clones, each corresponds to a gene for which a mutant phenotype is known. The expected phenotypes are detected with RNAi, but not in each experiment, indicating false-negative results. The bacterial clones are indicated by ‘GenePairs Name' (name of genepair used to PCR-amplify a genomic fragment) and ‘Predicted Gene' (predicted gene targeted by the named genepair). ‘Locus' gives the genetic locus; ‘Known Mutant Phenotype' gives the mutant phenotype for the indicated gene described in the literature. The RNAi phenotypes are defined in the Materials and Methods section

In conclusion, we find that RNAi results from different laboratories and from experiments done in the same laboratory vary from 10% to 30%. This appears to be due to a high frequency of false negatives in each RNAi screen, even when the same method is used in the same laboratory.

The Genome-Wide RNAi Screen
Based on the positive results of the Chromosome I screen using the rrf-3 strain, we next screened the complete RNAi library with rrf-3 mutant animals. We obtained results for 16,401 clones and detected phenotypes for 2,079 (12.7%). Of these, we identified phenotypes for 625 clones for which no phenotype was reported in the Fraser et al. (2000) or Kamath et al. (2003) screens using N2, with the remaining 1,454generating phenotypes in both screens (Table S1). In addition, there are 287 clones for which only Fraser et al. (2000) or Kamath et al. (2003) found phenotypes (23 of these were not done in our screen).

The clones for which we only detected an RNAi phenotype once and that were specific for the rrf-3 screen were retested. Subsequently, the phenotypes of the clones corresponding to Chromosomes II to X that were not confirmed by this repetition were tested once more. In this way, the clones specific for the rrf-3 screen had two chances to be confirmed. Of the 625 clones for which no phenotype was found in the Fraser et al. (2000) and Kamath et al. (2003) N2 screens, the phenotypes of 423 clones were confirmed and 202 remained unconfirmed (Table 2; see Table S1). Combining the N2 screens and these 423 clones, the percentage of clones with a phenotype increases from 10.3% to 12.8%.

Table 2 Genome-Wide RNAi
Summary of the bacterial clones that induced detectable RNAi phenotypes (‘Positive Clones'). For 423 clones, RNAi phenotypes were reproducibly detected in our laboratory using rrf-3, but no RNAi phenotypes were reported in the N2 screens; 1,454 clones induced phenotypes in both laboratories; 264 were specifically detected by Fraser et al. (2000) or Kamath et al. (2003). For 202 clones, RNAi phenotypes were detected with rrf-3 and no RNAi phenotypes were reported in the N2 screens, but this result could not be repeated. In addition, there are 23 clones for which we did not obtain results that gave a phenotype with N2. In the column with the overlapping clones, the rrf-3 data are mainly from one experiment, whereas the N2 data reported by Fraser et al. (2000) and Kamath et al. (2003) are from repeated experiments. The phenotypes that were scored are described in the Materials and Methods section

Some of the RNAi phenotypes only found with rrf-3 that remained unconfirmed could be confirmed by RNAi phenotypes detected with other clones of the RNAi library corresponding to the same gene or by other laboratories using different RNAi methods. For example, for the clones corresponding to the predicted genes F56D1.1 (a member of the zinc finger C2H2-type protein family) and F27C8.6 (a member of the esterase-like protein family), we detected sterile progeny (Stp) and embryonic lethality (Emb), respectively; these were also found by Piano et al. (2002). In addition, some unconfirmed RNAi phenotypes are confirmed by comparing to phenotypes of genetic mutants such as gpc-2, hlh-8, and unc-84. This suggests that many of the unconfirmed phenotypes reflect true gene functions.


Analysis of the rrf-3 Results
To validate the results obtained using rrf-3, we first assayed the rate of false positives in the total dataset (all RNAi results obtained with rrf-3 for the 16,401 clones tested). In the assay used by Kamath et al. (2003), a set of genes for which it is known that genetic mutants display no lethality was selected. A false positive in the RNAi data is then defined as detecting a lethal RNAi phenotype for any of these genes. In the N2 screen, the false-positive rate was 0.4%. We find that the false-positive rate in the rrf-3 data is similarly low (0 of 152 genes).

To further determine the effectiveness of the screen, we compared the RNAi phenotypes with loss-of-function phenotypes of genetic mutants. For all chromosomes except for Chromosome I, the rrf-3 data were confirmed by refeeding only if there was no phenotype detected in the N2 screens by Fraser et al. (2000) or Kamath et al. (2003). Therefore, to compare the difference in detection of known phenotypes between the rrf-3 and the N2 screens, we used the Chromosome I datasets, where phenotypes were confirmed independently for the two strains. Of 75 genetic loci on Chromosome I, Fraser et al. (2000) detected 48% of published phenotypes, compared to 59% for rrf-3 (Table S2). Using the genome-wide rrf-3 dataset (excluding the 202 unconfirmed phenotypes), we detected the published phenotype for 54% of 397 selected loci, compared to 52% for N2 (Table 3; see Table S2).

Table 3 Effectiveness of the rrf-3 Screen
RNAi phenotypes obtained with rrf-3 (confirmed using N2 data or rrf-3 refeeding), and the N2 screens by Fraser et al. (2000) or Kamath et al. (2003) were compared with those of genes that have known loss-of-function phenotypes. ‘Total Genetic Loci Scored' denotes the number of genes that were analysed by RNAi. All loci have a loss-of-function phenotype that was detectable in our screen. ‘RNAi Phenotype Detected' gives the number of genes for which a phenotype was identified. ‘Published Phenotype Detected' gives the number of genes for which the RNAi phenotype matched the phenotype described in the literature

We next asked whether using the rrf-3 strain improved general phenotype detection or whether certain types of phenotypes were particularly increased compared to the N2 screens by Fraser et al. (2000) and Kamath et al. (2003). To do this, we analysed the detection rate of different types of Chromosome I loci. First, we looked at a set of 23 loci with nonlethal postembryonic mutant phenotypes. Using rrf-3, we reproducibly detected the published phenotype for 11 of these compared to only two for N2. Of 50 loci required for viability (essential genes), we detected 31 using rrf-3, compared to 33 for N2. Thus, detection of essential genes was similar in the two strains, but detection of postembryonic phenotypes was improved with rrf-3. Finally, for the whole genome using rrf-3, we reproducibly detected the published phenotypes for 34 genetic mutants for which no RNAi phenotype was reported in the N2 screens (nine essential genes, 21 with postembryonic mutant phenotypes, and four with a slow-growth mutant phenotype). By comparison, published phenotypes were detected for 23 loci only with N2 (16 essential genes and seven with postembryonic mutant phenotypes) (see Table S2). We conclude that rrf-3 particularly improves detection of genes with postembryonic mutant phenotypes, a class that is poorly detected using wild-type N2.

A striking feature of the rrf-3 dataset is the high number of clones where a slow or arrested growth (Gro/Lva) defect was induced, without associated embryonic lethality or sterility. Overall, 619 clones induced a Gro/Lva defect using rrf-3, compared to 276 for N2, whereas the number of essential genes detected was similar (1,040 versus 1,170, respectively). In addition, in the confirmed set of 423 clones with rrf-3-specific phenotypes, Gro/Lva defects are the largest category (42%), whereas this is only 18% for N2, with the largest category being essential genes (49%). These data suggest that rrf-3 might particularly enhance detection of genes that mutate to a slow-growth phenotype; we cannot easily test this hypothesis, as there are currently few known loci with this mutant phenotype. In some cases, a Gro/Lva phenotype was seen in rrf-3, whereas a different phenotype was seen in N2 (e.g., either lethality or a weak postembryonic phenotype). This suggests that some of the Gro/Lva phenotypes detected are due to incomplete RNAi of an essential gene (where lethality was seen in N2) or by a stronger RNAi effect (where no growth defect was seen in N2). In addition, it is possible that some of the Gro/Lva phenotypes detected are synthetic effects of using the rrf-3 mutant strain.

To summarise, using the rrf-3 RNAi supersensitive strain in large-scale screens increases the percentage of clones for which it is possible to detect a phenotype. Detection of postembryonic phenotypes is particularly increased, whereas detection of essential genes is similar in rrf-3 and N2. In addition, using rrf-3, there is a high rate of induction of Gro/Lva defects.

Positional Cloning of Genetic Mutants with Visible Phenotypes
Despite the advantages of RNAi, genetic mutants remain indispensable for many experiments. In the past decades, forward genetic screens identified a large number of genetic mutants, many of which are not yet linked to the physical map. We used the RNAi phenotypes obtained with the genome-wide screens to test whether we could systematically clone genes that are mutated in existing genetic mutants. First, the genetic map positions of all uncloned genetic mutants with visible phenotypes were checked using WormBase (http://www.wormbase.org, the Internet site for the genetics, genomics, and biology of C. elegans). Second, we searched for clones near the defined map positions that, when fed to N2, rrf-3, or both, gave phenotypes corresponding to the phenotypes of the genetic mutants. For most genetic mutants, more than ten clones with a similar phenotype were found in the interval to which the genetic mutant was mapped. However, for 21 genetic mutants, only one or a few candidate clones were found. The genes corresponding to these clones were subsequently sequenced in the genetic mutant to determine whether a mutation was present. In total, we sequenced 42 predicted genes for the 21 genetic mutants (Table S3). For seven of these—bli-3, bli-5, dpy-4, dpy-6, dpy-9, rol-3, and unc-108—we found a mutation in one of the sequenced genes (Table 4). The mutated gene was confirmed by sequencing the same gene in a second or third allele (or both) of these genetic mutants (Table 4).

Table 4 Properties of the Genetic Mutants Cloned Using the RNAi Phenotypic Data
Genetic mutants were linked to the physical map using RNAi phenotypes. The ‘Genetic Map Position’ is based on WormBase annotation. ‘Mutated Gene’ denotes the predicted gene, which is mutated in the genetic mutant. ‘RNAi Phenotype’ gives the loss-of-function phenotype either using rrf-3 or N2 (the latter is based on findings of Kamath et al. [2003]). The phenotypes that were scored are described in the Materials and Methods section


a 
dpy-6(e2762) has a deletion that removes the first six amino acid residues (aa) of the eighth exon and part of the seventh intron


b Multiple mutations in dpy-6(f11) (5′-tcgAaaa[G/T]tt[C/A]aaccccacgccaact[G/T]cc); the AAA→AAAA mutation at position 2792 bp of the F16F9.2 coding sequence causes a frameshift that results in a premature stop in the fifth exon

The identification of mutations in unc-108 encoding the homolog of the small GTPase Rab2 is of particular interest. The RNAi phenotype of this gene gives a clue about the genetic property of the mutations in the mutants of unc-108. With rrf-3, we find that inactivation of Rab2 (F53F10.4) by RNAi causes uncoordinated movement (Table 4). Mutations in unc-108 were isolated in a screen for dominant effects on behaviour; heterozygous unc-108 mutants display dominant movement defects and are indistinguishable from homozygous mutants (Park and Horvitz 1986). RNAi phenocopies a loss-of-function phenotype, suggesting that the dominant movement defects of unc-108 mutants may be due to haplo-insufficiency. In eukaryotes, Rab2 is involved in regulating vesicular trafficking between the endoplasmic reticulum and Golgi. Based on the movement defects of unc-108 mutants, UNC-108 might be involved in vesicle transport in neurons that regulate locomotion. Thus, the RNAi data are a powerful tool to facilitate rapid cloning of the genes identified by genetic mutants and will provide important starting points for further studies of their function.

Discussion
With this genome-wide RNAi screen using the hypersensitive strain rrf-3, we have significantly increased the functional information on the C. elegans genome, and we confirmed many RNAi phenotypes observed previously. We have assigned RNAi phenotypes for 406 genes (corresponding to the 423 extra clones) using rrf-3. For 13 genes, Kamath et al. (2003) or Fraser et al. (2000) had already found a phenotype using a different clone from the RNAi library that targeted the same gene, and for at least 44 genes a genetic mutant exists (see Table S2). Other investigators have also found RNAi phenotypes for some of the genes using different methods. However, for most genes our result is to our knowledge the first hint about their biological function.

Although we have identified new RNAi phenotypes for a substantial number of genes, others will have been missed in our screen for the following reasons. First, besides its increased sensitivity to RNAi, the rrf-3 strain has an increased incidence of males (Him) and displays slightly increased embryonic lethality and a reduced brood size (Simmer et al. 2002). In our rrf-3 experiments, we therefore made some minor adaptations to the original RNAi protocol described by Fraser et al. (2000). We did not score for the Him phenotype and had more stringent criteria for embryonic lethality and sterility. This may have reduced the number of extra clones identified with a phenotype. Moreover, the changes in the protocol can also account for some differences in the detection of RNAi phenotypes between rrf-3 and N2. Second, when an RNAi phenotype is detected with N2 and not with rrf-3, the lack of a detectable phenotype may be the result of variability in the efficiency of RNAi. This is consistent with the fact that we observe differences between experiments done with the same strain.

When an RNAi phenotype is detected with rrf-3 and not with N2, this can be due to the increased sensitivity to RNAi of rrf-3. However, besides the higher sensitivity, we may also be observing synthetic effects with rrf-3 (e.g., embryonic lethality, sterility, or developmental delay). In particular, a large number of clones induced a developmental delay phenotype using rrf-3. Synthetic effects cannot be excluded without investigating genetic mutants. Again, variability in the efficiency of RNAi will also contribute to these differences, and a small portion may be false positives. In general, the few false positives that occur in the screen are most likely due to experimental errors, whereas the false negatives are due to reduced efficiency of the RNAi. Finally, differences between rrf-3 and N2 do not only involve the absence and presence of an RNAi phenotype, but also differences in the phenotypes for clones that did induce phenotypes in both screens (e.g., embryonic lethal in one screen and a postembryonic phenotype in the other). For example, we detected for unc-112 a 100% embryonic lethal (Emb) phenotype with rrf-3, whereas Kamath et al. (2003) detected an adult lethal (Adl), uncoordinated (Unc), and paralyzed (Prz) phenotype with N2. Conversely, Kamath et al. (2003) detected for gon-1 a 100% Emb phenotype and other phenotypes with N2, while we did not detect an Emb phenotype with rrf-3.

What could be the source of the interexperimental variation of RNAi? Different phenotypes for the same gene can possibly occur owing to slight differences in the developmental stage at which the animals are exposed to dsRNA and owing to changes in temperature during the experiment. However, this probably does not account for the differences we see, as we always used animals of the same larval stage (L3/L4) and used incubators for constant temperature. It was shown previously that the level of induction of dsRNA production by isopropylthio-β-D-galactoside (IPTG) can modify the penetrance of the RNAi phenotype (Kamath et al. 2000). The