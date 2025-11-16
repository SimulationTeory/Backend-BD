CREATE TABLE dbo.TiemposDetalle (
    id_detalle INT IDENTITY(1,1) PRIMARY KEY,
    id_tiempos INT NOT NULL,
    nodo_inicio VARCHAR(20) NOT NULL,
    nodo_fin VARCHAR(20) NOT NULL,
    a FLOAT NOT NULL,
    m FLOAT NOT NULL,
    b FLOAT NOT NULL,
    FOREIGN KEY (id_tiempos) REFERENCES dbo.TiemposSet(id_tiempos)
);

CREATE TABLE dbo.Simulacion (
    id_simulacion INT IDENTITY(1,1) PRIMARY KEY,
    nombre_proyecto NVARCHAR(100) NOT NULL,
    id_tiempos INT NOT NULL,
    duracion_A FLOAT NULL,
    ruta_critica_A NVARCHAR(MAX) NULL,
    duracion_B FLOAT NULL,
    ruta_critica_B NVARCHAR(MAX) NULL,
    FOREIGN KEY (id_tiempos) REFERENCES dbo.TiemposSet(id_tiempos)
);

CREATE INDEX IX_Simulacion_id_tiempos ON dbo.Simulacion(id_tiempos);

CREATE TABLE dbo.Actividad (
    id_actividad INT IDENTITY(1,1) PRIMARY KEY,
    id_simulacion INT NOT NULL,
    id_detalle INT NOT NULL,
    te FLOAT NOT NULL,
    varianza FLOAT NOT NULL,
    FOREIGN KEY (id_simulacion) REFERENCES dbo.Simulacion(id_simulacion) ON DELETE CASCADE,
    FOREIGN KEY (id_detalle) REFERENCES dbo.TiemposDetalle(id_detalle)
);

CREATE INDEX IX_Actividad_id_simulacion ON dbo.Actividad(id_simulacion);

CREATE TABLE dbo.NodoSimulacion (
    id_nodo INT IDENTITY(1,1) PRIMARY KEY,
    id_simulacion INT NOT NULL,
    nodo INT NOT NULL,
    early FLOAT NOT NULL,
    late FLOAT NOT NULL,
    holgura FLOAT NOT NULL,
    critical BIT NOT NULL,
    tipo CHAR(1) NOT NULL,
    FOREIGN KEY (id_simulacion) REFERENCES dbo.Simulacion(id_simulacion) ON DELETE CASCADE
);

CREATE INDEX IX_NodoSimulacion_id_simulacion ON dbo.NodoSimulacion(id_simulacion);

CREATE TABLE dbo.Resultado (
    id_resultado INT IDENTITY(1,1) PRIMARY KEY,
    id_simulacion INT NOT NULL,
    varianza_total FLOAT NULL,
    desviacion FLOAT NULL,
    probabilidad_30_sem FLOAT NULL,
    FOREIGN KEY (id_simulacion) REFERENCES dbo.Simulacion(id_simulacion) ON DELETE CASCADE
);

CREATE INDEX IX_Resultado_id_simulacion ON dbo.Resultado(id_simulacion);
