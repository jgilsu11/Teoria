--seleccionar lo clientes que mas han gastado y EL número de canciones que han comprado (motrar solo los 5 primeros Y LO QUE HA GASTADO)


SELECT "FirstName" 
FROM "Customer" c 
WHERE "CustomerId" IN (
	SELECT *
		FROM "Invoice" i 
		WHERE "InvoiceId" IN(
			SELECT *
				FROM "InvoiceLine" il 
				WHERE 
		
		
		)
)


--Como se ha corregido en clase (PERO NO VALE UNITPRICE * QUANTITY PORQUE HAY Q AGRUPAR INVOICEID )
--Esto es para poder guardar la query con otro nombre por si la necesito más tarde pero es temporal si se cierra DBeaver se pierden. Para que no se pierda se usan VISTAS

CREATE TEMPORARY TABLE TablaGastosCanciones5 AS 
SELECT count(il."TrackId") AS NumeroCanciones, sum(i."Total") AS TotalGastado, concat(c."FirstName", ' ', c."LastName") AS NombreCompleto, sum(il."UnitPrice" * il."Quantity") AS TotalGastado2
FROM "Customer" c    --El NATURAL JOIN nO hace falta especificar donde se tienen que unir (Solo se puede utilizar si por donde unen tienen el mismo nombre y si solo coinciden 1 )
NATURAL JOIN "Invoice" i 
NATURAL JOIN "InvoiceLine" il
GROUP BY c."CustomerId" 
ORDER BY TotalGastado
LIMIT 5;

SELECT  *
FROM TablaGastosCanciones5;

--Creamos la vista

CREATE  VIEW VistaGastosCanciones5 AS 
SELECT count(il."TrackId") AS NumeroCanciones, sum(i."Total") AS TotalGastado, concat(c."FirstName", ' ', c."LastName") AS NombreCompleto, sum(il."UnitPrice" * il."Quantity") AS TotalGastado2
FROM "Customer" c    --El NATURAL JOIN nO hace falta especificar donde se tienen que unir (Solo se puede utilizar si por donde unen tienen el mismo nombre y si solo coinciden 1 )
NATURAL JOIN "Invoice" i 
NATURAL JOIN "InvoiceLine" il
GROUP BY c."CustomerId" 
ORDER BY TotalGastado
LIMIT 5;

SELECT * FROM VistaGastosCanciones5;




--Subconsultas en el FROM modulariza el código y es más rápida

--Calcular los clientes que han gastado más de 20$ sin subconsulta

SELECT sum("Total") AS Total, "CustomerId" 
FROM "Invoice" i 
GROUP BY "CustomerId" 
HAVING Sum("Total") > 20;

--Con subconsulta (Así nos permite hacer el where)

SELECT * FROM (
			SELECT sum("Total") AS Total, "CustomerId" 
				FROM "Invoice" i 
				GROUP BY "CustomerId") AS TablaGastos
WHERE Total > 20;



/**
 * encontrar los generos con más canciones (solo los que tengan más de 50 canciones
 *  y devolver el nombre del género y el número de canciones 
 */**
 
 
 --Sin subconsulta
 
 SELECT count("Quantity") AS NumCanciones, g."Name"
 FROM "Genre" g  
 INNER JOIN "Track" t  ON t."GenreId" = g."GenreId" 
 INNER JOIN "InvoiceLine" il  ON t."TrackId" = il."TrackId" 
 GROUP BY g."GenreId"
 HAVING count("Quantity") >50
 ORDER BY NumCanciones DESC;

--Con subconsulta

SELECT  * FROM(
			 SELECT count("Quantity") AS NumCanciones, g."Name"
				 FROM "Genre" g  
				 INNER JOIN "Track" t  ON t."GenreId" = g."GenreId" 
				 INNER JOIN "InvoiceLine" il  ON t."TrackId" = il."TrackId"
				 GROUP BY g."GenreId") AS TotalCancionesGrabadas
WHERE NumCanciones >50
ORDER BY NumCanciones DESC;


/**
 Artistas con ventas mayores a 100$ sumando las ventas de sus albumes
 */
--Sin subconsulta

SELECT sum(il."UnitPrice") AS SumaVentasArtistas, a."Name"  AS NombreArtista
FROM "Artist" a 
INNER JOIN "Album" a2 ON a."ArtistId" = a2."ArtistId" 
INNER JOIN "Track" t  ON a2."AlbumId" = t."AlbumId"
INNER JOIN "InvoiceLine" il ON t."TrackId" =il."TrackId" 
GROUP BY a."ArtistId" 
HAVING sum(il."UnitPrice") > 100
ORDER BY sum(il."UnitPrice") DESC;

--Con subconsulta en el from


SELECT * FROM (
			SELECT sum(il."UnitPrice") AS SumaTotal, a."Name"  AS NombreArtista
				FROM "Artist" a 
					INNER JOIN "Album" a2 ON a."ArtistId" = a2."ArtistId" 
					INNER JOIN "Track" t  ON a2."AlbumId" = t."AlbumId"
					INNER JOIN "InvoiceLine" il ON t."TrackId" =il."TrackId" 
					GROUP BY a."ArtistId") AS VentasArtistas
WHERE SumaTotal > 100;


/**
 Clientes que han comprado más de 5 canciones en total
 */
--Sin subconsulta


SELECT count(il."TrackId") AS NumeroCanciones, concat(c."FirstName", ' ', c."LastName") AS NombreCompleto
FROM "Customer" c 
INNER JOIN "Invoice" i ON c."CustomerId" = i."CustomerId" 
INNER JOIN "InvoiceLine" il ON i."InvoiceId" = il."InvoiceId" 
GROUP BY c."CustomerId" 
HAVING count(il."TrackId") > 5
ORDER BY NumeroCanciones DESC;

--Con subconsulta en from

SELECT * FROM(
			SELECT count(il."TrackId") AS NumeroCanciones, concat(c."FirstName", ' ', c."LastName") AS NombreCompleto
				FROM "Customer" c 
				INNER JOIN "Invoice" i ON c."CustomerId" = i."CustomerId" 
				INNER JOIN "InvoiceLine" il ON i."InvoiceId" = il."InvoiceId" 
				GROUP BY c."CustomerId")
WHERE NumeroCanciones > 5
ORDER BY NumeroCanciones;


/**
 OVER PARTITION BY                 es una funcion ventana que sirve para realizar funciones de agregación más complejas y reducir 
                                   la info sin reducir las filas en la tabla (agrupa los datos sin reducir las filas (genera una columna más)
                                   en la tabla resultado (no modifica la original)
 */
--Calcular el Total de ingresos por pais 
--Normal (Reduce el numero de filas)

SELECT "BillingCountry", sum("Total") AS SumaTotalIngresos 
FROM "Invoice" i 
GROUP BY "BillingCountry" 

--Usando el OVER PARTITION BY (No reduce el numero de filas) Nos permite no perder el resto de info
	
SELECT "BillingCountry", sum("Total") OVER (PARTITION BY "BillingCountry") AS TotalPais, i."Total"     --El PARTITION BY es como nuestro GROUP by
FROM "Invoice" i 
ORDER BY i."Total" DESC; 


--Total de gastos de cada cliente teniendo la info de sus facturas

SELECT  "FirstName" AS Nombre,  "InvoiceDate", "Total" AS TotalDia, sum(i."Total") OVER (PARTITION BY i."CustomerId") AS TotalGastosCliente , "BillingCountry" 
FROM "Invoice" i
INNER JOIN "Customer" c ON i."CustomerId" = c."CustomerId"


-- calcula la duracion acumulada de las canciones dentro de cada genero ordenandolas por su duración
SELECT g."Name" AS Genero, t."Name" AS Cancion , sum(t."Milliseconds") OVER (PARTITION BY g."GenreId" ORDER BY t."Milliseconds" DESC)/60000 AS Totalminutos, t."Milliseconds"/60000 AS minutos
FROM "Genre" g 
INNER JOIN "Track" t ON g."GenreId" = t."GenreId"; 

/**

 ROW_NUMBER  es para asignar un número a cada fila
 La diferencia entre RANK y ROW_NUMBER es que si empatan el primero y sgeundo ROW te los pone 112 y el RANK 113 (EL rank se lo salta y row no)
 
 Mirar si row nos da empates y en tal caso hacer rank para que nos devuelva 
 
 */
--Numerar los albums por orden alfabetico

SELECT *
FROM (
	SELECT ROW_NUMBER () OVER (ORDER BY "Title") AS ranking, "Title" 
		FROM "Album" a) AS TablaOrden
WHERE ranking = 2;

--Numerar las canciones por cada album en funcion de su duracion(mi intento)

SELECT ROW_NUMBER () OVER (ORDER BY DuracionByAlbum) AS ranking, NombreCancion, NombreAlbum, DuracionByAlbum
FROM (
	SELECT t."Name" AS NombreCancion, a."Title" AS NombreAlbum, sum(t."Milliseconds") OVER (PARTITION BY a."AlbumId" ) AS DuracionByAlbum 
		FROM "Album" a 
		INNER JOIN "Track" t ON a."AlbumId" = t."AlbumId") 



SELECT t."Name" AS NombreCancion, a."Title" AS NombreAlbum, sum(t."Milliseconds") OVER (PARTITION BY a."AlbumId" ) AS DuracionByAlbum 
FROM "Album" a 
INNER JOIN "Track" t ON a."AlbumId" = t."AlbumId"

--Corregido

SELECT ROW_NUMBER () OVER (PARTITION BY a."AlbumId" ORDER BY t."Milliseconds") AS filas, a."Title" AS NOMBREALBUM, T."Name" AS NOMBRECANCION, t."Milliseconds" AS DURACION
FROM "Album" a 
INNER JOIN "Track" t ON a."AlbumId" = t."AlbumId"
WHERE 
--Para sacar un valor en concreto
SELECT *
FROM (
	SELECT ROW_NUMBER () OVER (PARTITION BY a."AlbumId" ORDER BY t."Milliseconds") AS filas, a."Title" AS NOMBREALBUM, T."Name" AS NOMBRECANCION, t."Milliseconds" AS DURACION
		FROM "Album" a 
		INNER JOIN "Track" t ON a."AlbumId" = t."AlbumId")
WHERE filas= 2

--Numerar los clientes segun el total(sin agregar que han gastado(mi intento)

SELECT  ROW_NUMBER ()  OVER (PARTITION BY c."CustomerId" ORDER BY i."Total" DESC) AS TotalClientes,c."FirstName",  i."Total", "InvoiceDate"
FROM "Customer" c 
INNER JOIN "Invoice" i ON c."CustomerId" = i."CustomerId" 

--Correcion

SELECT *
FROM(
	SELECT ROW_NUMBER () OVER (PARTITION BY c."CustomerId" ORDER BY i."Total" DESC),  c."FirstName", i."Total", "InvoiceDate"
       FROM "Customer" c 
       NATURAL JOIN "Invoice" i ) AS Tabla
/**

