create or replace function k(idk int)
return integer
begin
return (select basic+hra from emp where id= idk);
end;
/