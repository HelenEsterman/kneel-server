CREATE TABLE `Metals`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `metal` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

CREATE TABLE `Styles`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `style` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

CREATE TABLE `Sizes`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `caret` NUMERIC(5,2) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

CREATE TABLE `Orders`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `metalId` INTEGER NOT NULL,
    `styleId` INTEGER NOT NULL,
    `sizeId` INTEGER NOT NULL,
    FOREIGN KEY(`metalId`) REFERENCES `Metals`(`id`),
    FOREIGN KEY(`styleId`) REFERENCES `Styles`(`id`),
    FOREIGN KEY(`sizeId`) REFERENCES `Sizes`(`id`)
);

INSERT INTO `Metals` VALUES (null, 'Sterling Silver', 12.42);
INSERT INTO `Metals` VALUES (null, '14K Gold', 736.4);
INSERT INTO `Metals` VALUES (null, '24K Gold', 1258.9);
INSERT INTO `Metals` VALUES (null, 'Platinum', 795.45);
INSERT INTO `Metals` VALUES (null, 'Palladium', 1241);

INSERT INTO `Styles` VALUES (null, 'Classic', 500);
INSERT INTO `Styles` VALUES (null, 'Modern', 710);
INSERT INTO `Styles` VALUES (null, 'Vintage', 965);

INSERT INTO `Sizes` VALUES (null, 0.5, 405);
INSERT INTO `Sizes` VALUES (null, 0.75, 782);
INSERT INTO `Sizes` VALUES (null, 1, 1470);
INSERT INTO `Sizes` VALUES (null, 1.5, 1997);
INSERT INTO `Sizes` VALUES (null, 2, 3638);

INSERT INTO `Orders` VALUES (null, 1, 2, 3);
INSERT INTO `Orders` VALUES (null, 3, 2, 1);

SELECT * FROM `Metals`;
SELECT * FROM `Sizes`;
SELECT * FROM `Styles`;
SELECT * FROM `Orders`;


SELECT * FROM `Metals`;
SELECT
                    o.id,
                    o.metalId,
                    o.sizeId,
                    o.styleId,
                    s.id style_id,
                    s.style,
                    s.price
                    FROM `Orders` o
                    LEFT JOIN Styles s
                    ON o.styleId = s.id
                    WHERE o.id = 1;


