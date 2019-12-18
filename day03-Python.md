# Python(2019.12.18.wed)

1. [파이썬설치](https://www.python.org/)

   * Add Python 3.8 to PATH 체크하기

2. `TIL`폴더 밑에 `Python` 폴더 설치

   1. `Git Bash here` -만들어둔 파이썬 파일 실행하기

      ```bash
      $python --version 하면
      Python 3.8.0출력됨
      ```

   2. `open with code`

      * PYTHON 디렉토리에 `README.md`추가 -파이썬 파일 만들기

        ```python
        # Python 101
        ## 1. 저장
        ## 2. 조건
        ## 3. 반복
        ```

      * `numbers.py`파일 생성 `install` `install`
        `TERMINAL`은 휴지통 눌러서 지워주기

3. `numbers.py`
   1. ```python
      # Python 101
      ## 1. 저장
      a=7
      b=3 
      
      print(a)
      print(a-b)
      print(a*b)
      print(a/b)
      print(a//b) #몫
      print(a%b) #나머지-짝수 홀수 일 때 b=2 써서 많이 씀.
      ```

   2. bash에서 확인

      ```bash
      $ python numbers.py
      7
      10
      4
      21
      2.3333333333333335
      2
      1 출력됨
      ```

      * 파이썬 자료형: 숫자,글자, 참거짓
      * 파이썬 주석처리 #

   3. 캐시파일 처리

      `new file` `.gitignore`

      ```python
      __pycache__/
      ```

   4. 

