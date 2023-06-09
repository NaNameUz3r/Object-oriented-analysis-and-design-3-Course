Идеальный цикл объектно-ориентированного анализа, проектирования и реализации состоит из семи шагов: 
Шаг 1. Определяем границы разрабатываемой системы (анализ):

- что будет включено в систему, а что точно не надо в неё включать;
- главные подсистемы;
- пользовательские метафоры (что именно пользователь/заказчик понимает под тем, что в рамках проекта он называет, например, "Автомобиль" или "Товар" или "Клиент");
- функциональность;
- библиотеки повторного использования. 

Задание 2.

Выполните этот шаг без детализации, по 3-7 ключевых понятий в компактной формулировке по каждому пункту. 

---

# Что будет включено в систему, а что точно не надо в неё включать.

1. Будет включено:

- Срабатывание событий (рутин) станции, на основании текущего состояния станции (наличие типов активных модулей станции, количество и статус астронавтов, некоторое количество рандомных рутин, не зависящих от выше упомянутых оснований);
- Сущность задач и целей игры (Построить определенные модули, прожить N дней, освоить X технологии);
- Сущность событийного журнала — как приятный элемент интерфейса для мониторинга событий и измненеия состояний станции;
- Сущности, описывающие модуль(и) станции;
- Cущности, описывающие астронавтов;
- Связь между ресурсами, сущностями их генерирующими и сущностями их потребляющими;
- Сущность таймера, и связь с ресурсами и рутинами, для координации событий в системе;
- Сущность экран, и связь с состоянем(ями) сущностей, которые отображает экран;
- Сущность сохраняющая текущее состояние системы в файл сохранения;

2. Не будет включено:

- Сложных сценариев генерации событий (рутин) станции (см. пункт 1 в блоке выше);
- Избыточная логика в "прокачке" астронавтов и модулей. Эти сущности должны иметь определенные характиристики и постоянные статусы, для связи с рутинами;
- Графические компоненты высокой сложности (Анимации и прочее);
- Клиент-серверная архитектура. Проект должен быть монолитным single-player симулятором;
- Режимы сложности. На этапе разработки MVP и иерархии типов это может сильно усложнить реализации АТД.
- Расширенная физика, точнее — физика вообще. Симулятор представляет собой text\event based симулятор с простым интерфейсом. 

# Главные подсистемы  

1. Модульная подсистема:
- Класс StationModule и его конкретные реализации для каждого модуля станции.
- Связи между модулями для определения зависимостей и взаимодействий между ними.

2. Астронавтская подсистема:
- Класс Astronaut и его конкретные реализации для каждого астронавта.
- Связи между астронавтами и модулями, чтобы определить их расположение и взаимодействие с модулями.
- Назначение астронавтов на выполнение рутин и учет их состояния.

3. Рутинная подсистема:
- Класс Routine и его конкретные реализации для различных рутин.
- Взаимодействие рутин с модулями, астронавтами и ресурсами, включая требования по времени и ресурсам для выполнения рутины.

4. Ресурсная подсистема:
- Класс Resource и его конкретные реализации для различных ресурсов.
- Учет и управление количеством ресурсов на станции, их генерацией и потреблением.

5. Временная подсистема:
- Класс Timer для отслеживания и управления временем на станции.
- Связи с рутинами и ресурсами для координации событий и выполнения задач.

6. Интерфейсная подсистема:
- Класс Screen или аналогичный, отвечающий за отображение информации на экране.
- Взаимодействие с другими сущностями для получения данных и обновления экрана.

7. Система управления:
- Класс SpaceStation или аналогичный, который объединяет все компоненты системы и отслеживает их состояние.
- Предоставление информации о состоянии станции и ее компонентах.

# Пользовательские метафоры (что именно пользователь/заказчик понимает под тем, что в рамках проекта он называет, например, "Автомобиль" или "Товар" или "Клиент");

- Игра ― процесс развития станции, учатие в реакции на события, принятие пользователем решений;
- Астронавт;
- Станция — совокупность модулей станции;
- Квест — текущая цель\задача;
- Сохранение — процесс сохранения текущего состояния игры;
- Загрузка — восстановление состояние игры из сохранения;
- Геймовер — невыполнение основной задачи, смерть всех астронавтов, разрушение ключевых модулей станции;
- Воздух, вода, еда, энергия, медицина, запчасти — названия ресурсов;

# Функциональность
-  Создание и управление станцией;
-  Управление ресурсами;
-  Уход за астронавтами;
-  Выполнение рутин и задач;
-  Развитие и технологии;
-  Управление событиями и кризисами;
-  Интерфейс и визуализация;
-  Прогресс и достижения;
-  Сохранение и загрузка;


