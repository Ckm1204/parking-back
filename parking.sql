CREATE DATABASE parking;
USE parking;


CREATE TABLE Parqueadero (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL UNIQUE,
    nit INT,
    direccion VARCHAR(100) NOT NULL,
    telefono VARCHAR(10) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE Usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(150) NOT NULL UNIQUE,
    password VARCHAR(128) NOT NULL,
    last_login DATETIME,
    is_superuser BOOLEAN NOT NULL,
    first_name VARCHAR(150),
    last_name VARCHAR(150),
    email VARCHAR(254),
    is_staff BOOLEAN NOT NULL,
    is_active BOOLEAN NOT NULL,
    date_joined DATETIME NOT NULL,
    parqueadero_id INT,
    direccion VARCHAR(100) NOT NULL,
    telefono VARCHAR(100) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (parqueadero_id) REFERENCES Parqueadero(id) ON DELETE 	cascade
);

CREATE TABLE Tarifa (
    id INT AUTO_INCREMENT PRIMARY KEY,
    parqueadero_id INT,
    tamano VARCHAR(100) NOT NULL,
    precio INT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (parqueadero_id) REFERENCES Parqueadero(id) ON DELETE cascade
);

CREATE TABLE Propietario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombres VARCHAR(100) NOT NULL,
    identificacion VARCHAR(12) NOT NULL UNIQUE,
    email VARCHAR(254) NOT NULL,
    edad INT DEFAULT 18,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE Vehiculo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    propietario_id INT,
    parqueadero_id INT,
    placa VARCHAR(8) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (propietario_id) REFERENCES Propietario(id) ON DELETE cascade,
    FOREIGN KEY (parqueadero_id) REFERENCES Parqueadero(id) ON DELETE cascade
);

CREATE TABLE EntradaSalida (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tarifa_id INT,
    vehiculo_id INT,
    usuario_id INT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (tarifa_id) REFERENCES Tarifa(id) ON DELETE cascade,
    FOREIGN KEY (vehiculo_id) REFERENCES Vehiculo(id) ON DELETE cascade,
    FOREIGN KEY (usuario_id) REFERENCES Usuario(id) ON DELETE cascade
);