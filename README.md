# Abstract

The number of people experiencing homelessness in the United States is growing, and there are serious consequences for living unsheltered. At the same time, federal, state, and local governments devote a substantial amount of funding to addressing this persistent problem. Given this growth, governments may need to be more efficient with existing funding. To that end, recent advances leveraging machine learning and optimization by Kube et al., (2023) promise to more efficiently allocate scarce housing interventions to households. However, governments bound by legal and ethical constraints may not be able to implement these solutions if efficiency gains come at the cost of violating the Fair Housing Act. In this paper, we advance the work by Kube et al. (2023) in the following ways: 
1.	We derive the relationship between the optimal allocation of housing interventions to households and the conditional average treatment effect.
2.	We document where the Department of Housing and Urban Development's policy may not align with the goal of achieving the greatest number of exits from homelessness.
3.	We develop a simple exploratory data analysis technique for determining when allocating interventions to maximize exits from homelessness may violate the Fair Housing Act.
4.	We develop a method for dynamically addressing potential disproportionate assignments of housing interventions by Protected Classes, thereby ensuring the Fair Housing Act is not violated. 