## ML OPS, ФТиАД, Корякин Алексей

### Как собирать и выкладывать

```bash
docker build  -t ml-homework .
docker tag ml-homework sampledockerusername/ml-homework
docker push
```

### Как использовать 
```bash
docker pull sampledockerusername/ml-homework
docker compose up
```

Что есть: 
* Базовый набор API
* Управляющий записью/считыванием моделей класс
* Docker image на докерхабе 
* docker-compose c зачатками появления БД
