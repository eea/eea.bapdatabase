USE `bap`;

INSERT INTO Narrative (Country, Objective, Ident) VALUES ('Austria', 'Objective1', 'A1_2');
INSERT INTO Narrative (Country, Objective, Ident) VALUES ('Austria', 'Objective2', 'A2_1');
INSERT INTO Narrative (Country, Objective, Ident) VALUES ('Austria', 'Objective2', 'A2_2');
INSERT INTO Narrative (Country, Objective, Ident) VALUES ('Austria', 'Objective2', 'A2_4');
INSERT INTO Narrative (Country, Objective, Ident) VALUES ('Austria', 'Objective5', 'A5_2');
INSERT INTO Narrative (Country, Objective, Ident) VALUES ('Austria', 'Objective6', 'A6_1');
INSERT INTO Narrative (Country, Objective, Ident) VALUES ('Austria', 'Objective7', 'A7_2');
INSERT INTO Narrative (Country, Objective, Ident) VALUES ('Austria', 'Objective9', 'A9_1');
INSERT INTO Narrative (Country, Objective, Ident) VALUES ('Austria', 'Objective9', 'A9_3');
INSERT INTO Narrative (Country, Objective, Ident) VALUES ('Austria', 'Objective9', 'A9_4');
INSERT INTO Narrative (Country, Objective, Ident) VALUES ('Austria', 'Measure1', 'B1_1');
INSERT INTO Narrative (Country, Objective, Ident) VALUES ('Austria', 'MandE', 'C1_3');

INSERT INTO `TargetActions` (`Target`,`Action`,`Objective`) VALUES ('A5_2', 'A5_2_2', 'Objective5');
INSERT INTO `TargetActions` (`Target`,`Action`,`Objective`) VALUES ('A6_1', 'A6_1_1', 'Objective6');
INSERT INTO `TargetActions` (`Target`,`Action`,`Objective`) VALUES ('C1_3', 'C1_3_1', 'MandE');


INSERT INTO QuestionsText (`Ident`, `FullText`) VALUES ('A1_2', 'Target: A1.2: Sufficiency, coherence, connectivity and resilience of the protected areas network in the EU substantially enhanced by 2010 and further enhanced by 2013 (cf objective 9, target 9.4).');
INSERT INTO QuestionsText (`Ident`, `FullText`) VALUES ('A2_1', 'Target: A.2.1 Member States have optimised use of opportunities under agricultural, rural development and forest policy to benefit biodiversity 2007-2013');
INSERT INTO QuestionsText (`Ident`, `FullText`) VALUES ('A2_2', 'Target: A.2.2 Risks to soil biodiversity in EU substantially reduced by 2013.');
INSERT INTO QuestionsText (`Ident`, `FullText`) VALUES ('A2_4', 'Target: A.2.4 Principal pollutant pressures on terrestrial and freshwater biodiversity substantially reduced by 2010, and again by 2013.');
INSERT INTO QuestionsText (`Ident`, `FullText`) VALUES ('A5_2', 'Target: A.5.2 Impact of alien genotypes on biodiversity in the EU significantly reduced by 2010 and again by 2013.');
INSERT INTO QuestionsText (`Ident`, `FullText`) VALUES ('A6_1', 'Target: A.6.1: International governance for biodiversity substantially more effective in delivering positive biodiversity outcomes by 2010');
INSERT INTO QuestionsText (`Ident`, `FullText`) VALUES ('A7_2', 'Target: A.7.2 EU mainstream external development assistance delivering enhanced biodiversity and related livelihoods benefits, and negative impacts on biodiversity prevented or minimised, from 2006 onwards.');
INSERT INTO QuestionsText (`Ident`, `FullText`) VALUES ('A9_1', 'Target: A.9.1 8% reduction in greenhouse gas emissions achieved by 2010.');
INSERT INTO QuestionsText (`Ident`, `FullText`) VALUES ('A9_3', 'Target: A.9.3 Climate change adaptation or mitigation measure from 2006 onwards delivering biodiversity benefits, and any negative impacts on biodiversity prevented or minimised, from 2006 onwards.');
INSERT INTO QuestionsText (`Ident`, `FullText`) VALUES ('A9_4', 'Target: A.9.4 Resilience of EU biodiversity to climate change substantially strengthened by 2010.');
INSERT INTO QuestionsText (`Ident`, `FullText`) VALUES ('B1_1', 'Target: B1.1: Adequate funding provided for Natura 2000, biodiversity outside Natura 2000 in EU, biodiversity in external assistance and biodiversity research, inventory and monitoring 2007-2013');
INSERT INTO QuestionsText (`Ident`, `FullText`) VALUES ('C1_3', 'Target: C.1.3: Monitoring providing adequate data flow for implementation of indicator set, for reporting on favourable conservation status, and for broader assessment of effectiveness of this Action Plan by 2010.');


-- INSERT INTO QuestionsText (`Ident`, `FullText`) VALUES ('xxx', 'xxx');

