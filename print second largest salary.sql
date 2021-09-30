SELECT max(salary)
from emp
group BY salary
ORDER BY salary DESC LIMIT 1,1;
