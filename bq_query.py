#Query the project where there is the biggest usage of Keys :
SELECT
   SUM(value)as totalCount, projectId
FROM
   'my-project.mydataset.mytable'
GROUP BY projectId
ORDER BY totalCount DESC

#Query the Keys that have not been used since the last 30 days:
SELECT
   keyid,
   LastUse
   FROM (
      SELECT
         keyid,
         MAX(start) AS LastUse
      FROM
         'my-project.mydataset.mytable'
      GROUP BY keyid
      ORDER BY LastUse DESC )
WHERE LastUse < TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 30 day)