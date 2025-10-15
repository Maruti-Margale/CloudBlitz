#practice
create table demo (name varchar(200));
use demo;

#DDL

create table demo (name varchar(200));
alter table demo add column id int(10);

alter table demo modify column name int(10);

alter table demo drop column name;

alter table demo rename to demoooo;

alter table demoooo rename column id to idd;

truncate table demoooo;

drop table demoooo;

select * from demoooo;

#DML
use empp;

select * from empp where salary = 10;

select * from empp where salary = 10 or department = 'IT';

select * from empp where salary > 50000 and department = 'IT';

select * from empp where salary > 50000 and not department = 'IT';

select * from empp where salary > 60000 and department in('Analyst');

insert into empp() values(15,'dondu','kondu','bhondu@123',1234567890,2345,'AWS');

update empp set salary = 0 where emp_id = 15;

delete from empp where emp_id = 15;

select * from empp;

#DCL

grant select,insert on empp to username;

revoke insert on empp from username;


#TCL

rollback;

commit;