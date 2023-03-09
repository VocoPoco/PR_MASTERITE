CREATE TABLE `User` (
	`id` INT(255) NOT NULL AUTO_INCREMENT,
	`first` varchar(255) NOT NULL,
	`last` varchar(255) NOT NULL,
	`email` varchar(255) NOT NULL UNIQUE,
	`password` varchar(255) NOT NULL,
    `type` TINYINT(1) NOT NULL CHECK (`type` IN (0, 1)),
	PRIMARY KEY (`id`)
);

CREATE TABLE `Tutorial` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`name` varchar(255) NOT NULL,
	`level` varchar(255) NOT NULL,
	`description` varchar(255) NOT NULL,
	`order` varchar(255) NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `Progress` (
	`user_id` INT NOT NULL,
	`tutorial_id` INT NOT NULL,
	`progress` INT NOT NULL
);

CREATE TABLE `tutorial_steps` (
	`id` INT(255) NOT NULL AUTO_INCREMENT,
	`tutorial_id` INT(255) NOT NULL,
	`name` varchar(255) NOT NULL,
	`content` varchar(255) NOT NULL,
	`link` varchar(255) NOT NULL,
	PRIMARY KEY (`id`)
);

ALTER TABLE `Progress` ADD CONSTRAINT `Progress_fk0` FOREIGN KEY (`user_id`) REFERENCES `User`(`id`);

ALTER TABLE `Progress` ADD CONSTRAINT `Progress_fk1` FOREIGN KEY (`tutorial_id`) REFERENCES `Tutorial`(`id`);

ALTER TABLE `tutorial_steps` ADD CONSTRAINT `tutorial_steps_fk0` FOREIGN KEY (`tutorial_id`) REFERENCES `Tutorial`(`id`);