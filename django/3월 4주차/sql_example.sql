-- 주석

-- 모든 정보를 조회.
SELECT * FROM users_user;

-- Table 생성
CREATE TABLE classmates (
  id INTEGER PRIMARY KEY,
  name TEXT
);

-- 테이블 삭제
DROP TABLE classmates;

-- Table 생성
CREATE TABLE classmates (
  -- id INTEGER PRIMARY KEY,
  -- 이 친구가 설정되면 rowid는 자동생성이 되지 않는다.
  -- 그래서 PK 컬럼은 직접 작성하기 보다 자동생성되는 rowid를 사용하는 것이 좋다.
  -- but 장고는 rowid를 사용하지 않는다! tmi!!!
  name TEXT,
  age INT,
  address TEXT
);

-- 데이터 추가
INSERT INTO classmates (name, age, address)
-- 테이블 생략했는데 밸류값을 임의로 순서 변경하면 안 된다~!
VALUES ('Hong Gil Dong', 30, 'Seoul');

CREATE TABLE classmates (
  -- id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  age INT NOT NULL,
  address TEXT NOT NULL
);

INSERT INTO classmates
VALUES ('Hong Gil Dong', 30, 'Seoul');

INSERT INTO classmates
VALUES ('Hong', 23, 'Seoul'),
('Kong', 23, 'Dae'),
('Long', 23, 'Gwang'),
('CHong', 23, 'Gumi');

-- id, name 만 가져 온다면
SELECT rowid, name FROM classmates;

-- id, name 을 하나만 가져오고 싶다면
SELECT rowid, name FROM classmates LIMIT 1;

-- id, name 을 세번째 값 하나만 가져온다면, OFFSET은 0부터 시작!!!
-- LIMIT 는 열이고, OFFSET은 행인가???
SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2;

-- 주소가 서울인 사람만 가져온다면
SELECT rowid, name FROM classmates
WHERE address='Seoul';


INSERT INTO classmates
VALUES ('Hong', 50, 'Busan');

SELECT DISTINCT name FROM classmates
WHERE name='Hong';

-- 4번 데이터가 먼저 지워졌으면 다음번에는 4번부터 데이터가 들어온다.(재사용)
-- 또 장고는 이런 재사용이 없다.
-- AUTOICREMENT 는 rowid 랑 다른 게 메모리 공간을 사용하고 재사용을 안해서 사용 안 한다.
-- 근데 또 장고에서는 저걸 사용한다. 어이가 없네 장고는 왜 반대로만 가는거지


-- 데이터 수정
UPDATE classmates
SET address='Seoul'
WHERE rowid=1


CREATE TABLE articles (
  title TEXT NOT NULL,
  content TEXT NOT NULL);

INSERT INTO articles
VALUES ('1번 글', '1번글 내용');

ALTER 테이블 이름 변경

ALTER TABLE articles
ADD COLUMN updated_at TEXT;

INSERT INTO articles
VALUES ('title', 'content', datetime('now'));