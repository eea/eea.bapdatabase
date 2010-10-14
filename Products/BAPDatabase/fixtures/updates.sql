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

INSERT INTO `objectives` (`id`,`name`,`description`) VALUES	(1,'Objective1','To safeguard the EU\'s most important habitats and species');
INSERT INTO `objectives` (`id`,`name`,`description`) VALUES	(2,'Objective2','To conserve and restore biodiversity and ecosystem services in the wider EU countryside');
INSERT INTO `objectives` (`id`,`name`,`description`) VALUES	(3,'Objective3','To conserve and restore biodiversity and ecosystem services in the wider EU marine environment');
INSERT INTO `objectives` (`id`,`name`,`description`) VALUES	(4,'Objective4','To reinforce compatibility of regional and territorial development with biodiversity in the EU');
INSERT INTO `objectives` (`id`,`name`,`description`) VALUES	(5,'Objective5','To substantially reduce the impact on EU biodiversity of invasive alien species (IAS) & alien genotypes');
INSERT INTO `objectives` (`id`,`name`,`description`) VALUES	(6,'Objective6','To substantially strengthen effectiveness of international governance for biodiversity and ecosystem services');
INSERT INTO `objectives` (`id`,`name`,`description`) VALUES	(7,'Objective7','To substantially strengthen support for biodiversity and ecosystem services in EU external assistance');
INSERT INTO `objectives` (`id`,`name`,`description`) VALUES	(8,'Objective8','To substantially reduce the impact of international trade on global biodiversity and ecosystem services');
INSERT INTO `objectives` (`id`,`name`,`description`) VALUES	(9,'Objective9','To support biodiversity adaptation to climate change');
INSERT INTO `objectives` (`id`,`name`,`description`) VALUES	(10,'Objective10','To sustainably strengthen the knowledge base for conservation and sustainable use of biodiversity, in the EU and globally');
INSERT INTO `objectives` (`id`,`name`,`description`) VALUES	(11,'Measure1','Ensuring adequate financing for biodiversity');
INSERT INTO `objectives` (`id`,`name`,`description`) VALUES	(12,'Measure2','Strengthening EU decision making for biodiversity');
INSERT INTO `objectives` (`id`,`name`,`description`) VALUES	(13,'Measure3','Building partnerships for biodiversity');
INSERT INTO `objectives` (`id`,`name`,`description`) VALUES	(14,'Measure4','Building public education, awareness and participation for biodiversity');
INSERT INTO `objectives` (`id`,`name`,`description`) VALUES	(15,'MandE','Monitoring, evaluation and review');
# 15 records

#
# Alter table structure for table 'Narrative'
#

ALTER TABLE Narrative ADD PRIMARY KEY (`Country`, `Objective`, `Ident`, `MOP`);

#
# Alter table structure for table 'QuestionsText'
#

ALTER TABLE QuestionsText ADD PRIMARY KEY (`ID`);