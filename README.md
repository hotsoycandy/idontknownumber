# idontknownumber (나숫자몰라요)

## description (설명)

"나숫자몰라요" 는 python을 기반으로 만들어진 웹앱으로써 사용자가 적은 숫자가 어떤 숫자인지 판단하기 위해 만들어졌습니다.

django를 기반으로 한 서버를 실행하며 사용자가 브라우저를 통해 접속했을 경우 단순 HTML을 반환합니다.

HTML 페이지에서는 사용자가 그린 숫자 그림을 서버에 보낸 후 예측값을 받아 다시 페이지에 표시합니다.

숫자 인식 학습은 mnist 데이터를 기반으로 하며 처음 실행시켰을 경우 학습을 시작합니다.

학습이 끝난 후에는 가중치가 파일형태로 로컬에 저장되며 두 번째 실행할 때 부터는 학습하지 않고 저장된 가중치를 읽어옵니다.

## intsall (설치)

python@3.6.3 에서 작업하였으며 코드에서 사용하는 모듈들이 미리 pip을 통해 (혹은 다른 경로로) 미리 설치가 되어 있어야 합니다.

설치된 모듈들은 아래와 같으며 정확하지 않을 수 있으니 코드를 직접 참고하시길 바랍니다.

- django
- keras
- numpy
- pillow
- Matplotlib

## run (실행)

django 기본 설정에서 바뀐 것은 없습니다.

아래와 같이 입력후 http://localhost:8000 으로 접속합니다.

```
> python manage.py runserver
```

## feedback (피드백)

[git issue](https://github.com/hotsoycandy/idontknownumber/issues)를 통해 남겨주세요
