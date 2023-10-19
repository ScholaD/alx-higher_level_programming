-- creates the table unique_id on your MySQL server.
   -- unique_id description:
      -- id INT - default value 1, must be unique

CREATE TABLE IF NOT EXISTS unique_id
       (id INT DEFAULT 1,
       UNIQUE (ID),
       name VARCHAR(256));
