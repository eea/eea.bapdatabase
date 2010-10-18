USE `bap`;
#
# Table structure for table 'objectives'
#

DROP TABLE IF EXISTS `objectives`;

CREATE TABLE `objectives` (
  `id` INTEGER NOT NULL auto_increment,
  `name` varchar(100) default NULL,
  `description` varchar(255) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=innodb DEFAULT CHARSET=utf8;

SET autocommit=1;

#
# Dumping data for table 'objectives'
#

INSERT INTO `objectives` (`name`,`description`, `headline`) VALUES ('Objective1','To safeguard the EU\'s most important habitats and species','Biodiversity loss of most important habitats and species halted by 2010, these habitats and species showing substantial recovery by 2013');
INSERT INTO `objectives` (`name`,`description`, `headline`) VALUES ('Objective2','To conserve and restore biodiversity and ecosystem services in the wider EU countryside','In wider countryside (terrestrial, freshwater, brackish water outside Natura 2000 network), biodiversity loss halted by 2010 and showing substantial recovery by 2013.');
INSERT INTO `objectives` (`name`,`description`, `headline`) VALUES ('Objective3','To conserve and restore biodiversity and ecosystem services in the wider EU marine environment','In wider marine environment (outside Natura 2000 network), biodiversity loss halted by 2010 and showing substantial recovery by 2013');
INSERT INTO `objectives` (`name`,`description`, `headline`) VALUES ('Objective4','To reinforce compatibility of regional and territorial development with biodiversity in the EU','Regional and territorial development benefiting biodiversity, and negative impacts on biodiversity prevented and minimised or, where unavoidable, adequately compensated for, from 2006 onwards.');
INSERT INTO `objectives` (`name`,`description`, `headline`) VALUES ('Objective5','To substantially reduce the impact on EU biodiversity of invasive alien species (IAS) & alien genotypes','Negative impacts on EU biodiversity of IAS and alien genotypes prevented or minimised from 2010 onwards.');
INSERT INTO `objectives` (`name`,`description`, `headline`) VALUES ('Objective6','To substantially strengthen effectiveness of international governance for biodiversity and ecosystem services','');
INSERT INTO `objectives` (`name`,`description`, `headline`) VALUES ('Objective7','To substantially strengthen support for biodiversity and ecosystem services in EU external assistance','');
INSERT INTO `objectives` (`name`,`description`, `headline`) VALUES ('Objective8','To substantially reduce the impact of international trade on global biodiversity and ecosystem services','');
INSERT INTO `objectives` (`name`,`description`, `headline`) VALUES ('Objective9','To support biodiversity adaptation to climate change','Potential for damaging impacts, related to climate change, on EU biodiversity substantially reduced by 2013');
INSERT INTO `objectives` (`name`,`description`, `headline`) VALUES ('Objective10','To sustainably strengthen the knowledge base for conservation and sustainable use of biodiversity, in the EU and globally','');
INSERT INTO `objectives` (`name`,`description`, `headline`) VALUES ('Measure1','Ensuring adequate financing for biodiversity','');
INSERT INTO `objectives` (`name`,`description`, `headline`) VALUES ('Measure2','Strengthening EU decision making for biodiversity','');
INSERT INTO `objectives` (`name`,`description`, `headline`) VALUES ('Measure3','Building partnerships for biodiversity','');
INSERT INTO `objectives` (`name`,`description`, `headline`) VALUES ('Measure4','Building public education, awareness and participation for biodiversity','');
INSERT INTO `objectives` (`name`,`description`, `headline`) VALUES ('MandE','Monitoring, evaluation and review','');
# 15 records

#
# Alter table structure for table 'Narrative'
#

ALTER TABLE Narrative ADD PRIMARY KEY (`Country`, `Objective`, `Ident`, `MOP`);

#
# Alter table structure for table 'QuestionsText'
#

ALTER TABLE QuestionsText ADD PRIMARY KEY (`ID`);


# Dump of table TargetActions
# ------------------------------------------------------------

DROP TABLE IF EXISTS `TargetActions`;

CREATE TABLE `TargetActions` (
  `ID` int(11) NOT NULL auto_increment,
  `Target` varchar(255) default NULL,
  `Action` varchar(255) default NULL,
  `Objective` varchar(255) default NULL,
  PRIMARY KEY  (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `TargetActions` (`Target`,`Action`, `Objective`) VALUES ('A1_1','A1_1_1','Objective1');
INSERT INTO `TargetActions` (`Target`,`Action`, `Objective`) VALUES ('A1_1','A1_1_2','Objective1');
INSERT INTO `TargetActions` (`Target`,`Action`, `Objective`) VALUES ('A1_1','A1_1_3','Objective1');
INSERT INTO `TargetActions` (`Target`,`Action`, `Objective`) VALUES ('A1_2','A1_2_3','Objective1');
INSERT INTO `TargetActions` (`Target`,`Action`, `Objective`) VALUES ('A1_3','A1_3_1','Objective1');
INSERT INTO `TargetActions` (`Target`,`Action`, `Objective`) VALUES ('A2_1','A2_1_1','Objective2');
INSERT INTO `TargetActions` (`Target`,`Action`, `Objective`) VALUES ('A2_1','A2_1_3','Objective2');
INSERT INTO `TargetActions` (`Target`,`Action`, `Objective`) VALUES ('A2_1','A2_1_4','Objective2');
INSERT INTO `TargetActions` (`Target`,`Action`, `Objective`) VALUES ('A2_1','A2_1_6','Objective2');
INSERT INTO `TargetActions` (`Target`,`Action`, `Objective`) VALUES ('A2_1','A2_1_8','Objective2');
INSERT INTO `TargetActions` (`Target`,`Action`, `Objective`) VALUES ('A2_1','A2_1_9','Objective2');
INSERT INTO `TargetActions` (`Target`,`Action`, `Objective`) VALUES ('A2_1','A2_1_11','Objective2');
INSERT INTO `TargetActions` (`Target`,`Action`, `Objective`) VALUES ('A2_1','A2_1_12','Objective2');
INSERT INTO `TargetActions` (`Target`,`Action`, `Objective`) VALUES ('A2_1','A2_1_15','Objective2');
INSERT INTO `TargetActions` (`Target`,`Action`, `Objective`) VALUES ('A2_2','A2_2_2','Objective2');
INSERT INTO `TargetActions` (`Target`,`Action`, `Objective`) VALUES ('A2_3','A2_3_1','Objective2');
INSERT INTO `TargetActions` (`Target`,`Action`, `Objective`) VALUES ('A2_4','A2_4_1','Objective2');
INSERT INTO `TargetActions` (`Target`,`Action`, `Objective`) VALUES ('A2_4','A2_4_2','Objective2');
INSERT INTO `TargetActions` (`Target`,`Action`, `Objective`) VALUES ('A2_4','A2_4_3','Objective2');
INSERT INTO `TargetActions` (`Target`,`Action`, `Objective`) VALUES ('A3_1','A3_1_4','Objective3');
INSERT INTO `TargetActions` (`Target`,`Action`, `Objective`) VALUES ('A3_1','A3_1_5','Objective3');
INSERT INTO `TargetActions` (`Target`,`Action`, `Objective`) VALUES ('A3_2','','Objective3');
INSERT INTO `TargetActions` (`Target`,`Action`, `Objective`) VALUES ('A3_4','','Objective3');
INSERT INTO `TargetActions` (`Target`,`Action`, `Objective`) VALUES ('A3_5','A3_5_1','Objective3');
INSERT INTO `TargetActions` (`Target`,`Action`, `Objective`) VALUES ('A3_5','A3_5_2','Objective3');
INSERT INTO `TargetActions` (`Target`,`Action`, `Objective`) VALUES ('A3_5','A3_5_3','Objective3');
INSERT INTO `TargetActions` (`Target`,`Action`, `Objective`) VALUES ('A3_6','A3_6_1','Objective3');
INSERT INTO `TargetActions` (`Target`,`Action`, `Objective`) VALUES ('A3_6','A3_6_2','Objective3');
INSERT INTO `TargetActions` (`Target`,`Action`, `Objective`) VALUES ('A3_6','A3_6_3','Objective3');
INSERT INTO `TargetActions` (`Target`,`Action`, `Objective`) VALUES ('A3_7','A3_7_1','Objective3');
INSERT INTO `TargetActions` (`Target`,`Action`, `Objective`) VALUES ('A4_3','','Objective4');
INSERT INTO `TargetActions` (`Target`,`Action`, `Objective`) VALUES ('A4_4','A4_4_1','Objective4');
INSERT INTO `TargetActions` (`Target`,`Action`, `Objective`) VALUES ('A5_1','A5_1_2','Objective5');
INSERT INTO `TargetActions` (`Target`,`Action`, `Objective`) VALUES ('A5_1','A5_1_3','Objective5');
INSERT INTO `TargetActions` (`Target`,`Action`, `Objective`) VALUES ('A5_1','A5_1_4','Objective5');
INSERT INTO `TargetActions` (`Target`,`Action`, `Objective`) VALUES ('A7_1','A7_1_3','Objective7');
INSERT INTO `TargetActions` (`Target`,`Action`, `Objective`) VALUES ('A7_1','A7_1_4','Objective7');
INSERT INTO `TargetActions` (`Target`,`Action`, `Objective`) VALUES ('A7_2','A7_2_2','Objective7');
INSERT INTO `TargetActions` (`Target`,`Action`, `Objective`) VALUES ('A8_1','A8_1_3','Objective8');
INSERT INTO `TargetActions` (`Target`,`Action`, `Objective`) VALUES ('A8_1','A8_1_4','Objective8');
INSERT INTO `TargetActions` (`Target`,`Action`, `Objective`) VALUES ('A8_1','A8_1_8','Objective8');
INSERT INTO `TargetActions` (`Target`,`Action`, `Objective`) VALUES ('A9_1','A9_1_1','Objective9');
INSERT INTO `TargetActions` (`Target`,`Action`, `Objective`) VALUES ('A9_3','A9_3_2','Objective9');
INSERT INTO `TargetActions` (`Target`,`Action`, `Objective`) VALUES ('A9_4','A9_4_1','Objective9');
INSERT INTO `TargetActions` (`Target`,`Action`, `Objective`) VALUES ('A9_4','A9_4_3','Objective9');
INSERT INTO `TargetActions` (`Target`,`Action`, `Objective`) VALUES ('A10_1','A10_1_2','Objective10');
INSERT INTO `TargetActions` (`Target`,`Action`, `Objective`) VALUES ('A10_1','A10_1_8','Objective10');
INSERT INTO `TargetActions` (`Target`,`Action`, `Objective`) VALUES ('A10_1','A10_1_9','Objective10');
INSERT INTO `TargetActions` (`Target`,`Action`, `Objective`) VALUES ('B1_1','B1_1_1','Measure1');
INSERT INTO `TargetActions` (`Target`,`Action`, `Objective`) VALUES ('B1_1','B1_1_4','Measure1');
INSERT INTO `TargetActions` (`Target`,`Action`, `Objective`) VALUES ('B1_1','B1_1_8','Measure1');
INSERT INTO `TargetActions` (`Target`,`Action`, `Objective`) VALUES ('B2_4','','Measure2');
INSERT INTO `TargetActions` (`Target`,`Action`, `Objective`) VALUES ('B3_1','B3_1_2','Measure3');
INSERT INTO `TargetActions` (`Target`,`Action`, `Objective`) VALUES ('B3_1','B3_1_5','Measure3');
INSERT INTO `TargetActions` (`Target`,`Action`, `Objective`) VALUES ('B3_1','B3_1_6','Measure3');
INSERT INTO `TargetActions` (`Target`,`Action`, `Objective`) VALUES ('B3_1','B3_1_7','Measure3');
INSERT INTO `TargetActions` (`Target`,`Action`, `Objective`) VALUES ('B3_1','B3_1_8','Measure3');
INSERT INTO `TargetActions` (`Target`,`Action`, `Objective`) VALUES ('B4_1','B4_1_1','Measure4');
INSERT INTO `TargetActions` (`Target`,`Action`, `Objective`) VALUES ('B4_1','B4_1_2','Measure4');
INSERT INTO `TargetActions` (`Target`,`Action`, `Objective`) VALUES ('C1_2','C1_2_1','MandE');