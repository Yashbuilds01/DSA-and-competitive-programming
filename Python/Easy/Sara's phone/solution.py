def Phone(N,K,M):
   if (N*K)<M:
    return (-1)
   if M%K ==0:
    return (M//K)
   else:
     return (M//K) +1