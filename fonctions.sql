CREATE FUNCTION AddUser (username VARCHAR(32), utilisateur  )         
    LANGUAGE SQL  
    MODIFIES SQL
    BEGIN 

      INSERT INTO utilisateur VALUES (username)
    END 

