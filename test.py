import torch
x = torch.Tensor([[1,2],[2,3]])


d = x.unsqueeze(2)
c = x.unsqueeze(1)
e = torch.bmm(d,c)
print(c.size())
print(d.size())
print(e.size())

# from keras import backend as K
#
#
#
#
# d = K.expand_dims(x, 2)
# c = K.expand_dims(x, 1)
# e = K.batch_dot(d, c)
# print(e)