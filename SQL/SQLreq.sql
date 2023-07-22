1.

    SELECT * 
	FROM user_profiles
	WHERE name
    LIKE '%am%';
	
2.  SELECT expenses.totalCost, cars.id, cars.carBrandId
	FROM expenses
	INNER JOIN cars ON expenses.carId = cars.id
	WHERE cars.carBrandId = 1
	ORDER BY totalCost DESC;	

3.	SELECT COUNT(title)
	FROM car_models
	WHERE carBrandId IN ('1','2');
	
4.	SELECT COUNT(userId), carBrandId, carModelId
	FROM cars
	GROUP BY carBrandId, carModelId;




5.  SELECT name
	FROM user_profiles
	WHERE userId IN (SELECT userId FROM cars);