# Requirement 


# Reference 
아키텍처 Ref.
- https://github.com/cosmicpython/code

스키마매퍼 Ref.
- https://github.com/holinnn/lupin
- 아키텍처 : https://docs.hevodata.com/pipelines/data-flow-arch/


# 이기종 DB Migration 
1. 소스(Connector, DB, Table), 타겟(Connector, DB, Table)를 정의한다. 
- [정의방법]
  1) schema.json 파일 내에 소스와 타겟 정보를 정의한다. 
  2) 설정파일이 없다면, input을 직접 입력받는다. 
2. 소스와 타겟에 DB 접속이 가능한지 Connection 테스트를 한다. 
3. 타겟 테이블을 생성하기 위해 소스 테이블에 명시된 컬럼들의 DataType을 조회한다. 
- [규칙]
    - migration 컬럼이 있을 경우, 매핑된 컬럼이름으로 migration 한다. 
    - migration 컬럼이 없을 경우, 전체 컬럼을 migration 한다.
4. 타겟 테이블에 migration 용 테이블을 생성한다. 
- [생성규칙]
  - prefix 규칙 : [10자 미만의 영어 + 숫자만 체크]
  - subfix 규칙 : _YYYYMMDD_HHMM / _YYYYMMDD 
5. 소스 테이블에서 데이터를 조회하고, BULK INSERT문을 생성한다. 
6. 타겟 테이블에 데이터를 입력한다. 
7. 정상 테이터 입력이 되었는지 검증한다.
- [검증규칙]
  - 조회 수와 입력 수를 검증한다. 