#!/usr/bin/env python
# coding: utf-8

# # Exercícios NumPy  
# 
# Agora que aprendemos sobre NumPy, vamos testar seu conhecimento. Começaremos com algumas tarefas simples, para depois entrarmos nas perguntas mais complicadas.

# #### Importe NumPy como np

# In[1]:


import numpy as np


# #### Crie uma matriz de 10 zeros

# In[4]:


np.zeros(10)


# #### Crie uma matriz de 10 ones

# In[7]:


np.ones(10)


# #### Crie uma matriz de 10 cincos

# In[11]:


arr = np.arange(10)
arr[:] = 5
arr


# #### Crie um array de inteiros de 10 até 50

# In[12]:


np.arange(10,51)


# #### Crie um array dos numeros pares de 10 até 50

# In[16]:


np.arange(10,51,2)


# #### Criei uma matriz 3x3 com valores variando de 0 até 8

# In[20]:


arr = np.arange(0,9)
arr.reshape(3,3)


# #### Crie uma matriz identidade 3x3

# In[21]:


np.eye(3)


# #### Use NumPy para gerar números aleatórios entre 0 e 1

# In[23]:


np.random.rand(1)


# #### Use Numpy para gerar um array de 25 números aleatórios tirados de uma distribuição normal.

# In[25]:


np.random.randn(25)


# #### Crie a seguinte matriz:

# In[35]:


(np.arange(1,101) / 100).reshape(10,10)


# #### Crie um array de tamanho 20 igualmente espaçado entre 0 e 1.

# In[36]:


np.linspace(0,1,20)


# ## Indexação Numpy e Seleção
# 
# Agora você receberá algumas matrizes e será solicitado a replicar as saídas resultantes da matriz:

# In[38]:


mat = np.arange(1,26).reshape(5,5)
mat


# In[39]:


# ESCREVE O CÓDIGO AQUI QUE REPRODICA A SAÍDA DA CÉLULA ABAIXO
# SEJA CUIDADOSO PARA NÃO FUNCIONAR A CÉLULA ABAIXO, DE OUTRA FORMA, NÃO PODERÁ
# PODE VER A SORTEZA MAIS QUALQUER


# In[41]:


mat[2:,1:]


# In[29]:


# ESCREVE O CÓDIGO AQUI QUE REPRODICA A SAÍDA DA CÉLULA ABAIXO
# SEJA CUIDADOSO PARA NÃO FUNCIONAR A CÉLULA ABAIXO, DE OUTRA FORMA, NÃO PODERÁ
# PODE VER A SORTEZA MAIS QUALQUER


# In[42]:


mat[3][4]


# In[30]:


# ESCREVE O CÓDIGO AQUI QUE REPRODICA A SAÍDA DA CÉLULA ABAIXO
# SEJA CUIDADOSO PARA NÃO FUNCIONAR A CÉLULA ABAIXO, DE OUTRA FORMA, NÃO PODERÁ
# PODE VER A SORTEZA MAIS QUALQUER


# In[44]:


mat[0:3,1]


# In[31]:


# ESCREVE O CÓDIGO AQUI QUE REPRODICA A SAÍDA DA CÉLULA ABAIXO
# SEJA CUIDADOSO PARA NÃO FUNCIONAR A CÉLULA ABAIXO, DE OUTRA FORMA, NÃO PODERÁ
# PODE VER A SORTEZA MAIS QUALQUER


# In[46]:


mat[-1]


# In[32]:


# ESCREVE O CÓDIGO AQUI QUE REPRODICA A SAÍDA DA CÉLULA ABAIXO
# SEJA CUIDADOSO PARA NÃO FUNCIONAR A CÉLULA ABAIXO, DE OUTRA FORMA, NÃO PODERÁ
# PODE VER A SORTEZA MAIS QUALQUER


# In[47]:


mat[3:]


# ### Agora faça o seguinte

# #### Obter a soma de todos os valores no "mat"

# In[48]:


np.sum(mat)


# #### Obter o desvio padrão dos valores em mat

# In[49]:


mat.std()


# In[50]:


np.std(mat)


# #### Obter a soma de todas as colunas em mat

# In[54]:


mat.sum(axis = 0) # soma das colunas


# In[55]:


mat.sum(axis = 1) # soma das linhas


# In[57]:


print(mat.std(axis = 1))


# In[ ]:




