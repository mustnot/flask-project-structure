# Flask Project Structure

> 아직 미완인 부분이 많습니다. 좋은 구조에 대한 조언이 있으시다면 언제든지 해주셔도 좋습니다. 😀



## Concept.

전체적인 구조는 Django를 경험해보신 분들이라면 보자마자 비슷하다고 느낄 정도로 유사하게 만들어졌습니다. 개인적으로 아무리 마이크로 서비스 개발이 목적이더라도 단순히 몇 개의 파일에 모든 코드를 작성하는 방식을 선호하지 않습니다. 큰 프로젝트일 경우 서비스를 구성하는 각 애플리케이션이 다양할텐데, 이러한 각 애플리케이션을 잘 작성되고 분리되어 있다면 누구나 손쉽게 수정이 가능하고, 이를 분리하여 어느 서비스든 손쉽게 이식 가능하다고 믿고 있습니다.

```bash
├── myapp
│   ├── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── myproject
│   ├── __init__.py
│   ├── contrib
│   │   ├── __init__.py
│   │   ├── management
│   │   │   ├── __init__.py
│   │   │   └── runserver.py
│   │   └── register.py
│   ├── extensions
│   │   └── __init__.py
│   ├── handlers
│   │   ├── __init__.py
│   │   └── error_handler.py
│   ├── settings.py
│   ├── uwsgi.ini
│   └── wsgi.py
├── requirements.txt
└── manage.py
```



### myproject

* `settings.py` : Django와 비슷하게 `myproject` 폴더에 두어 각 환경에 대한 설정을 작성할 수 있게 했으며 아무래도 Flask는 `config.from_object` 메소드가 있다는 점에서 개인적으로 `Object` 형식으로 설정을 작성하는 것을 선호합니다.
* `manage.py` (개발중) : 다양한 매니징 기능을 제공하기 위해 현재 많은 구상을 하고 있는 부분입니다. 아직은 `runserver` 명령어 밖에 수행할 수 없지만, 점차 늘려갈 예정입니다. (😅)



### myapp

MVC 패턴을 고려한 개발 방식을 취했습니다. 아직 테스트 쪽은 효율적인 방법이 생각이 나지 않아 미완인 부분입니다.

* **M(model)** - `models.py` : **View**를 구성하는 **Model**을 작성하는 부분입니다.
* **V(view)** - `views.py` : 플라스크는 함수형 뷰타입이 조금 더 개발에 맡다고 생각합니다. 하지만 클래스형 뷰타입도 작성하여 적용 가능합니다.
* **C(controller)** -`urls.py` : **View**에서 작성된 뷰를 연결하는 곳으로 `url`, `func`, `method` 로 구분되어 있습니다.