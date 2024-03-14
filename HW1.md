1. Начнем с установки docker, потому что БД буду в нем запускать.
![docker-install.png](docker-install.png) 
2. Создаем Dockerfile с данными, которые будем использовать в дз. Данные взяты с https://www.kaggle.com/datasets/fivethirtyeight/uber-pickups-in-new-york-city \
![run-mongo.png](run-mongo.png) 
3. Запускаем контейнер \
![running-mongo.png](running-mongo.png) \
4. Заходим в контейнер и импортируем данные \ 
![import-data.png](import-data.png) \
5. Делаем R операции \
![read-find.png](read-find.png) \
![read-findOne.png](read-findOne.png) \
6. Делаем C операции \
![create-insertOne.png](create-insertOne.png) \
![create-insertMany.png](create-insertMany.png) 
7. Делаем U операции \
![update-one.png](update-one.png) \
8. Делаем D операции \
![delete-one.png](delete-one.png) \
![delete-many.png](delete-many.png) 
9. Сравним улучшение индекса на примере поиска записи, сначала найдем запись без индекса 
![withoutIndex.png](withoutIndex.png) 
10. Создадим индекс и найдем еще раз \
![createIndex.png](createIndex.png) \
11. Сравним время \
![findWithIndex.png](findWithIndex.png)
12. Видим, что в первый раз время исполнения(executionTimeMillis) составляло 823, а с индексом 19, что меньше на порядок=быстрее ищем=классно 
