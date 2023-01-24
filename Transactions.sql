-- Find the total number of transactions for each user
SELECT user_id, COUNT(*) as total_transactions
FROM transactions
GROUP BY user_id;

-- Find the average transaction value for each user
SELECT user_id, AVG(amount) as avg_transaction_value
FROM transactions
GROUP BY user_id;

-- Find the top 10 users with the highest total transaction value
SELECT user_id, SUM(amount) as total_transaction_value
FROM transactions
GROUP BY user_id
ORDER BY total_transaction_value DESC
LIMIT 10;

-- Find the percentage of transactions that were successful
WITH successful_transactions AS (
    SELECT COUNT(*) as successful_transactions
    FROM transactions
    WHERE status = 'success'
), total_transactions AS (
    SELECT COUNT(*) as total_transactions
    FROM transactions
)
SELECT (successful_transactions.successful_transactions / total_transactions.total_transactions) * 100 as success_rate
FROM successful_transactions, total_transactions;
