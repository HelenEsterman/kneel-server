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


if "metal" in url["query_params"]["_expand"]:
                sql = """
                    SELECT
                    o.id,
                    o.metalId,
                    o.sizeId,
                    o.styleId,
                    m.id metal_id,
                    m.metal,
                    m.price
                    FROM `Orders` o
                    LEFT JOIN Metals m
                    ON o.metalId = m.id
                    WHERE o.id = ?
                    """
                query_results = db_get_single(sql, pk)
                query_results_dict = dict(query_results)
                metal = {
                    "id": query_results_dict["metal_id"],
                    "metal": query_results_dict["metal"],
                    "price": query_results_dict["price"],
                }
                order = {
                    "id": query_results_dict["id"],
                    "metalId": query_results_dict["metalId"],
                    "sizeId": query_results_dict["sizeId"],
                    "styleId": query_results_dict["styleId"],
                    "metal": metal,
                }
                order_json_object = json.dumps(dict(order))
            elif "size" in url["query_params"]["_expand"]:
                sql = """
                    SELECT
                    o.id,
                    o.metalId,
                    o.sizeId,
                    o.styleId,
                    s.id size_id,
                    s.caret,
                    s.price
                    FROM `Orders` o
                    LEFT JOIN Sizes s
                    ON o.sizeId = s.id
                    WHERE o.id = ?
                    """
                query_results = db_get_single(sql, pk)
                query_results_dict = dict(query_results)
                size = {
                    "id": query_results_dict["size_id"],
                    "caret": query_results_dict["caret"],
                    "price": query_results_dict["price"],
                }
                order = {
                    "id": query_results_dict["id"],
                    "metalId": query_results_dict["metalId"],
                    "sizeId": query_results_dict["sizeId"],
                    "styleId": query_results_dict["styleId"],
                    "size": size,
                }
                order_json_object = json.dumps(dict(order))
            elif "style" in url["query_params"]["_expand"]:
                sql = """
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
                    WHERE o.id = ?
                    """
                query_results = db_get_single(sql, pk)
                query_results_dict = dict(query_results)
                style = {
                    "id": query_results_dict["style_id"],
                    "style": query_results_dict["style"],
                    "price": query_results_dict["price"],
                }
                order = {
                    "id": query_results_dict["id"],
                    "metalId": query_results_dict["metalId"],
                    "sizeId": query_results_dict["sizeId"],
                    "styleId": query_results_dict["styleId"],
                    "style": style,
                }
                order_json_object = json.dumps(dict(order))