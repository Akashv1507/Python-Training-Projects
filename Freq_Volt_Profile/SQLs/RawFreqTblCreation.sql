CREATE TABLE Raw_Frequency (
    id int NOT NULL AUTO_INCREMENT,
    Time_stamp Datetime NOT NULL,
    value float(6,4),
   	Unique(Time_stamp),
    PRIMARY KEY (id)
);