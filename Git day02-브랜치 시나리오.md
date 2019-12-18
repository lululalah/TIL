### 상황 1. fast-foward

###### feature/test 브랜치활용

> fast-foward는 feature 브랜치 생성된 이후 master 브랜치에 변경 사항이 없는 상황
>
> master은 앞으로 나아가기만 하면 됨.(master는 추가 변경사항 아직 없음)

1. feature/test branch 생성 및 이동

   ```bash
   $git checkout -b feature/test
   #feature/test 이름의 브랜치가 하나가 생김.
   ```

2. 작업 완료 후 commit

   ```bash
   $touch test.txt
   $git add test.txt
   $git commit -m 'Complete test'
   [feature/test ed2017a] Complete test
    1 file changed, 0 insertions(+), 0 deletions(-)
    create mode 100644 test.txt
   ```

3. master 이동

   ```bash
   (feature/test)에서 $git checkout master
   Switched to branch 'master'
   ```

4. master에 병합

   ```bash
   (master)에서 $git merge feature/test
   ```

5. 결과 -> fast-foward (단순히 HEAD를 이동)

   ```bash
   Updating aa777af..ed2017a
   Fast-forward
    test.txt | 0
    1 file changed, 0 insertions(+), 0 deletions(-)
    create mode 100644 test.txt
   ```

   * HEAD는 지금 내 위치를 뜻한다.

6. branch 삭제

   ```bash
   $git branch -d feature/test
   ```

   

------

### 상황 2. merge commit

###### feature/signout브랜치활용

> 서로 다른 이력(commit)을 병합(merge)하는 과정에서 다른 파일이 수정되어 있는 상황
>
> git이 auto merging을 진행하고, commit이 발생된다.

> master(원본)-feature-master(수정)-merge

1. feature/signout branch 생성 및 이동

   ```bash
   $git branch feature/signout #생성
   $git checkout feature/signout #이동
   $git checkout -b feature/signout #생성 및 이동
   ```

2. 작업 완료 후 commit

   ```bash
   $touch signout.html
   $git add signout.html
   $git commit -m 'Complete signout'
   
   [feature/signout 727bf52] Complete signout
    1 file changed, 0 insertions(+), 0 deletions(-)
    create mode 100644 signout.html
   
   
   $ git log --oneline
   727bf52 (HEAD -> feature/signout) Complete signout
   ed2017a (master) Complete test
   aa777af (feature/index) Complete index page
   8b44d1e Add README
   ```

3. master 이동

   ```bash
   $git checkout master
   ```

4. *master에 추가 commit 이 발생시키기!!*

   - **다른 파일을 수정 혹은 생성하세요!**

    ```bash
     (master)에서
     $touch hotfix.txt
     $git add .
     $git commit -m 'Hotfix on master'
     
     $git log --oneline
     37daafc (HEAD -> master) Hotfix on master
     ed2017a Complete test
     aa777af (feature/index) Complete index page
     8b44d1e Add README
    ```

5. master에 병합

   ```bash
   (master) $git merge feature/signout
   
   Merge made by the 'recursive' strategy.
    signout.html | 0
    1 file changed, 0 insertions(+), 0 deletions(-)
    create mode 100644 signout.html
   ```

6. 결과 -> 자동으로 *merge commit 발생*

   - **vim 편집기** 화면이 나타납니다.
     -노란글씨로 Merge branch 'feature/signout'
   - 자동으로 작성된 커밋 메시지를 확인하고, `esc`를 누른 후 `:wq`를 입력하여 저장 및 종료를 합니다.
     - `w` : write
     - `q` : quit
   - 커밋을 확인 해봅시다.

7. 그래프 확인하기

   ```bash
   $git log --oneline --graph
   ```

8. branch 삭제

   ```bash
   $git branch -d feature/signout
   ```

   

------

### 상황 3. merge commit 충돌

###### feature/board브랜치활용

> 서로 다른 이력(commit)을 병합(merge)하는 과정에서 동일 파일이 수정되어 있는 상황
>
> git이 auto merging을 하지 못하고, 해당 파일의 위치에 라벨링을 해준다.
>
> 원하는 형태의 코드로 직접 수정을 하고 merge commit을 발생 시켜야 한다.

1. feature/board branch 생성 및 이동

   ```bash
   $git checkout -b feature/board
   ```

   

2. 작업 완료 후 commit

   ```bash
   $touch board.html
   #README.md수정
   $git add .
   $git commit -m 'Complete board & Update README'
   ```

   ```bash
   $git log --oneline
   
   84ebbc3 (HEAD -> feature/board) Complete board & Update README
   6561379 (master) Merge branch 'feature/signout'
   37daafc Hotfix on master
   727bf52 Complete signout
   ed2017a Complete test
   aa777af (feature/index) Complete index page
   8b44d1e Add README
   ```

3. master 이동

   ```bash
   $git checkout master
   ```

4. *master에 추가 commit 이 발생시키기!!*

   * **동일 파일을 수정 혹은 생성하세요!**

    ```bash
     #README.md수정
     (master)에서
     $git add .
     $git commit -m 'Update README on master'
    ```

    ```bash
   $ git log --oneline
   a5b3e4b (HEAD -> master) Update README on master
   6561379 Merge branch 'feature/signout'
   37daafc Hotfix on master
   727bf52 Complete signout
   ed2017a Complete test
   aa777af (feature/index) Complete index page
   8b44d1e Add README
    ```

5. master에 병합

   ```bash
   $git merge feature/board
   ```

6. 결과 -> *merge conflict발생*

   ```bash
   Auto-merging README.md 
   CONFLICT (content): Merge conflict in README.md
   Automatic merge failed; fix conflicts and then commit the result.#자동병합 실패했고, 충돌 고친 다음에 commit해라.
   ```

   (master|MERGING)가 하늘색으로 나옴.

   

7. 충돌 확인 및 해결

   ```bash
   $git status
   On branch master
   You have unmerged paths.
     (fix conflicts and run "git commit")
     (use "git merge --abort" to abort the merge)
   
   Changes to be committed:
           new file:   board.html
   
   Unmerged paths:
     (use "git add <file>..." to mark resolution)
           both modified:   README.md
   
   ```

   * README.md 파일을 `Visual Studio Code`에서 수정하기.

     * 서로다르게 충돌났으니 개발자가 어떻게든 직접 고쳐라. git이 직접은 못고치겠음.
     * HEAD(현재상황), 아래에는 feature/board 변화 내역들이 각각 표시되어 있음.

     ```bash
     <<<<<<< HEAD
     master에서 추가함!
     =======
     merge commit-board.html생성
     >>>>>>> feature/board
     ```

     

8. merge commit 진행

   ```bash
   $ git commit
   ```

   - vim 편집기 화면이 나타납니다.
   - 자동으로 작성된 커밋 메시지를 확인하고, `esc`를 누른 후 `:wq`를 입력하여 저장 및 종료를 합니다.
     - `w` : write
     - `q` : quit
   - 커밋을 확인 해봅시다.

   ```bash
   $git commit
   ```

   

9. 그래프 확인하기

   ```bash
   $git log --oneline --graph
   ```

   

10. branch 삭제

    ```bash
    $git branch -d feature/board
    ```

    
