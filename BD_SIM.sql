USE SIMDB

CREATE TABLE SIMULACIONES (
	simulacion_ID VARCHAR(20) NOT NULL,
	fecha DATE NOT NULL,
	CONSTRAINT PK_SIMULACION_ID PRIMARY KEY (simulacion_ID)
);

DROP TABLE DETALLE_SIMULACIONES;

CREATE TABLE DETALLE_SIMULACIONES(
	simulacion_ID VARCHAR(20) NOT NULL,
	nodo varchar(10) NOT NULL,
	tiempo_Optimista int,
	tiempo_Mas_Probable int,
	tiempo_pesimista int,
	is_critical BIT,
	duracion_Semanas int NOT NULL,
	EF int,
	LF int,
	holgura int,
	CONSTRAINT FK_SIMULACION_ID FOREIGN KEY (simulacion_ID)
	REFERENCES SIMULACIONES(simulacion_ID)
);