SELECT t."Name", "UnitPrice"             --Esto sin subconsultas para sacar todas las canciones de AC/DC
FROM "Track" t
INNER JOIN "Album" a  ON  t."AlbumId"  =  a."AlbumId" 
INNER JOIN "Artist" a2   ON  a."ArtistId"  =  a2."ArtistId" 
WHERE  a2."Name" = 'AC/DC';




--Con subconsultas

SELECT *FROM "Track" t   --Hacemos un IN porque al ser dos NO se puede poner un igual
WHERE "AlbumId" IN(
	SELECT a."AlbumId"  
		FROM "Album" a 
		WHERE "ArtistId" = (
			SELECT "ArtistId"
				FROM "Artist" a2 
				WHERE "Name" = 'AC/DC');)
				
				
--Ejercicio2 Subconsulta   
--todos los clientes que tienen al menos una factura
--Primero sin subconjunto
				
SELECT "FirstName" 
FROM "Customer" c 
INNER JOIN "Invoice" i ON c."CustomerId" = i."CustomerId"
--Esto lo añadimos para que nos cuente las facturas
SELECT concat(c."FirstName", c."LastName") AS nombre_cliente, count(i."InvoiceId") AS numero_facturas 
FROM "Invoice" i 
INNER JOIN "Customer" c ON c."CustomerId" = i."CustomerId"
GROUP BY c."CustomerId" 
HAVING count(c."CustomerId") > 0

--Segundo con subconsulta
 
SELECT concat(c."FirstName", ' ', c."LastName") AS nombre_cliente 
FROM "Customer" c 
WHERE "CustomerId" IN(
	SELECT "CustomerId" 
		FROM "Invoice" i);
	
--Usando EXIST
	
SELECT concat(c."FirstName", ' ', c."LastName") AS nombre_cliente 
FROM "Customer" c       --EXIST hace que NO nos devuelva duplicados, es mas rápido y el WHERE se hace dentro de la subconsulta
WHERE EXISTS (
	SELECT "CustomerId" 
		FROM "Invoice" i 
		WHERE i."CustomerId"= c."CustomerId");

--EJEMPLO 3
--Sin subconsultas
SELECT concat(c."FirstName", c."LastName") AS nombre_cliente, count(i."InvoiceId") AS numero_facturas
FROM "Invoice" i 
INNER JOIN "Customer" c 
ON i."CustomerId" = c."CustomerId" 
GROUP BY c."CustomerId" 

--con subconsulta EN EL SELECT DEPENDIENDO DE QUE ES LO QUE QUEREMOS
SELECT(SELECT count("InvoiceId")
	   FROM "Invoice" i
	   WHERE i."CustomerId" = c."CustomerId")
FROM "Customer" c;



