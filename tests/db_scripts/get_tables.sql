DECLARE @catId INT
SET @catId = 8 -- CHANGE ME - run query to check intended ID - SELECT * FROM [CxDB].[dbo].[CategoriesTypes] WHERE Id > 7

SELECT * FROM [CxDB].[dbo].[CategoryForQuery] WHERE CategoryId in (SELECT Id FROM [CxDB].[dbo].[Categories] WHERE CategoryType = @catId)
SELECT * FROM [CxDB].[dbo].[Categories] WHERE CategoryType = @catId
SELECT * FROM [CxDB].[dbo].[CategoriesTypes] WHERE Id = @catId