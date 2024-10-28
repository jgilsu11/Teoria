CREATE TABLE IF NOT EXISTS estudiantes(    --IF NOT EXIST es por si ya la he creado y la vuelo a ejecutar para que NO me de error de que ya existe
id_estudiante SERIAL PRIMARY KEY,  
nombre VARCHAR(100) NOT NULL,      --VARCHAR permite un numero limitado de caracteres
email VARCHAR(100) UNIQUE NOT NULL,
genero CHAR(1) CHECK(genero IN ('M', 'F')),  --CHAR es permite menos caracteres
fecha_nacimiento DATE CHECK(fecha_nacimiento < CURRENT_DATE)
);


CREATE TABLE IF NOT EXISTS profesores(
id_profesor SERIAL PRIMARY KEY,
nombre VARCHAR(100) NOT NULL,
email VARCHAR(100) UNIQUE NOT NULL,
departamento VARCHAR(100) NOT NULL
);

--DROP TABLE cursos; --Esto es para cuando la has creado y NO se ha actualizado pues la eliminas y la vuelves a crear

CREATE TABLE cursos(
    id_curso SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    id_profesor INT NOT NULL,
    creditos INT CHECK (creditos > 0),
    FOREIGN KEY (id_profesor) 
        REFERENCES profesores(id_profesor)
        ON DELETE RESTRICT
        ON UPDATE CASCADE);


CREATE TABLE IF NOT EXISTS inscripciones(
id_inscripciones SERIAL PRIMARY KEY,
id_estudiante INT NOT NULL,
id_curso INT NOT NULL,
fecha_inscripcion DATE CHECK(fecha_inscripcion < CURRENT_DATE) NOT NULL,
nota FLOAT CHECK(0<= nota AND nota <= 10),
FOREIGN KEY (id_estudiante) REFERENCES estudiantes(id_estudiante) ON DELETE RESTRICT ON UPDATE CASCADE,
FOREIGN KEY (id_curso) REFERENCES cursos(id_curso) ON DELETE RESTRICT ON UPDATE CASCADE
);




INSERT INTO estudiantes (nombre, email, fecha_nacimiento, genero)   --NO se pone el id porque es serial y es auto incremental (se crea sola yendo ascendente)
VALUES ('Lola', 'lola@gmail.com', '2001-05-14', 'F');

INSERT INTO profesores (nombre, email, departamento)
VALUES ('Juanjo', 'juango@gmail.com', 'economia');

INSERT INTO cursos (nombre, id_profesor, creditos)
VALUES ('Analitics', 1 , 6);


SELECT * FROM estudiantes e 



UPDATE estudiantes 
SET fecha_nacimiento = '2000-05-14'    --Esto es para actualizar un dato en concreto por eso se usa el id
WHERE id_estudiante = 1;


UPDATE estudiantes 
SET email = 'lolalolita@gmail.com'
WHERE id_estudiante = 1;


SELECT * FROM estudiantes e    --El asterisco es por hacer referencia a todo

DELETE FROM estudiantes      --Esto es para eliinar un dato en concreto NO SE TE OLVIDE EL WHERE QU SINO BORRAS TODO
WHERE id_estudiante= 1;



ALTER TABLE estudiantes            --EL ALTER es para cambiar la estructura de la tabla (Aquí creamos una columna)
ADD COLUMN direccion VARCHAR(300);


ALTER TABLE estudiantes            --Aquí modifico cuantos caracteres puede tener email por eso se pone TYPE porq es una modificacion de tipo
ALTER COLUMN email TYPE VARCHAR(300);


ALTER TABLE estudiantes            --Aquí elimino una columna entera
DROP COLUMN direccion;
