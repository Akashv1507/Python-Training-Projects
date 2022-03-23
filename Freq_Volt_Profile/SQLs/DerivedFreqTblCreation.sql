CREATE TABLE derived_Frequency (
    id int NOT NULL AUTO_INCREMENT,
    DateKey Date NOT NULL,
    maximum float(4, 2),
    minimum float(4, 2),
    average float(4, 2),
    less_than_band float(4, 2),
    between_band float(4, 2),
    greater_than_band float(4, 2),
    out_of_band float(4, 2),
    out_of_band_inhrs float(4, 2),
    FDI float(4, 2),
   	Unique(DateKey),
    PRIMARY KEY (id)
);