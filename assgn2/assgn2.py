import matplotlib.pyplot as plt 
import numpy as np

### figure 0 ###
fig0 = plt.figure(0)
ax = fig0.add_subplot(111)
Q = np.arange(0,2,0.01)
MC = 1.70*Q - 0.83
UTC = 0.85*Q - 0.83
MR = -2.68*Q + 2.34
D = -1.34*Q + 2.34

mc, = ax.plot(Q,MC, label = 'mc')
mr, = ax.plot(Q,MR, label = 'mr')
utc, = ax.plot(Q,UTC, label = 'utc')
d, = ax.plot(Q,D, label='d')

q_opt = (0.83 + 2.34)/(1.70 + 2.68)
p_q = -1.34*q_opt + 2.34
utc_q = 0.85*q_opt - 0.83

eq_x, = ax.plot(q_opt+np.zeros(len(np.arange(-0.5,2.5,0.01))),np.arange(-0.5,2.5,0.01), '--',label = 'eq_x', color = 'r')
eq_y, = ax.plot(np.arange(0,0.73,0.01), p_q+np.zeros(len(np.arange(0,0.73,0.01))),'--',label = 'eq_y', color = 'b')
eq_y2, = ax.plot(np.arange(0,0.73,0.01), utc_q+np.zeros(len(np.arange(0,0.73,0.01))),'--',label = 'eq_y2', color = 'b')

area = plt.fill_between(np.arange(0,0.73,0.01),p_q+np.zeros(len(np.arange(0,0.73,0.01))), D[:len(np.arange(0,0.73,0.01))], color="0.8", hatch = "/")

area2 = plt.fill_between(np.arange(0,0.73,0.01),p_q+np.zeros(len(np.arange(0,0.73,0.01))), utc_q+np.zeros(len(np.arange(0,0.73,0.01))), color="0.6")

area2_value = "{0:.2f}".format(0.5*(q_opt)*(2.34 - p_q))

ax.set_xlim(0,2)
ax.set_ylim(-0.5,2.5)
ax.grid(True, linestyle='--')
ax.legend([mc,mr,utc,d,eq_x,eq_y,area2,area],['MC','MR','UTC','D','Optimum Quantity','Optimum Price','Profit ~ 1.37','Consumer Surplus ~'+str(area2_value)])
ax.set_ylabel('Price per quantity')
ax.set_xlabel('Quantity (in appropriate units)')


# ax.annotate('(0.72, 1.37)',xy=(0.72,1.37),xytext=(1.5,1),arrowprops=dict(arrowstyle="->",connectionstyle="angle3"))
# ax.set_xticks([5],minor=True)
# ax.set_xticklabels('5',color='r',minor=True)
# yticks = ax.yaxis.get_major_ticks()
# yticks[5].label.set_color('r')

plt.tight_layout()
fig0.savefig('images/sec1_1.png')

### figure 2 ###
fig2 = plt.figure(2)
ax = fig2.add_subplot(111)
Q = np.arange(0,2,0.01)
MC = 1.70*Q - 0.83
UTC = 0.85*Q - 0.83
D = -1.34*Q + 2.34

mc, = ax.plot(Q,MC, label = 'mc')
utc, = ax.plot(Q,UTC, label = 'utc')
d, = ax.plot(Q,D, label='d')

q_opt = (0.83 + 2.34)/(1.70 + 1.34)
p_q = -1.34*q_opt + 2.34


eq_x, = ax.plot(q_opt+np.zeros(len(np.arange(-0.5,2.5,0.01))),np.arange(-0.5,2.5,0.01), '--',label = 'eq_x', color = 'r')
eq_y, = ax.plot(np.arange(0,2,0.01), p_q+np.zeros(len(np.arange(0,2,0.01))),'--',label = 'eq_y', color = 'b')
area = plt.fill_between(np.arange(0,q_opt,0.01),p_q+np.zeros(len(np.arange(0,q_opt,0.01))), D[:len(np.arange(0,q_opt,0.01))], color="0.8", hatch = "/")
area_value = "{0:.2f}".format(0.5*(q_opt)*(2.34 - p_q))

ax.set_xlim(0,2)
ax.set_ylim(-0.5,2.5)
ax.grid(True, linestyle='--')
ax.legend([mc,utc,d,eq_x,eq_y,area],['MC','UTC','D','Optimum Quantity','Optimum Price','Consumer Surplus ~ '+str(area_value)])
ax.set_ylabel('Price per quantity')
ax.set_xlabel('Quantity (in appropriate units)')

plt.tight_layout()
fig2.savefig('images/sec1_3.png')

# ### figure 1 ###
fig1 = plt.figure(1)
ax = fig1.add_subplot(111)
Q = np.arange(-1,10,0.1)
MC = 3*Q**2 - 12*Q + 15
UTC = Q**2 - 6*Q + 15
MR = -16*Q + 32
D = -8*Q + 32

mc, = ax.plot(Q,MC, label = 'mc')
mr, = ax.plot(Q,MR, label = 'mr')
utc, = ax.plot(Q,UTC, label = 'utc')
d, = ax.plot(Q,D, label='d')


ax.set_xlim(0,5)
ax.set_ylim(0,35)
ax.grid(True, linestyle='--')

eq_x, = ax.plot(1.80+np.zeros(len(np.arange(0,36,1))),np.arange(0,36,1), '--',label = 'eq_x', color = 'r')
eq_y, = ax.plot(np.arange(0,1.9,0.1), 7.44+np.zeros(len(np.arange(0,1.9,0.1))),'--',label = 'eq_y', color = 'b')
eq_y2, = ax.plot(np.arange(0,1.9,0.1), 17.6+np.zeros(len(np.arange(0,1.9,0.1))),'--',label = 'eq_y', color = 'b')
area = plt.fill_between(np.arange(0,1.9,0.1),7.44+np.zeros(len(np.arange(0,1.9,0.1))), 17.6+np.zeros(len(np.arange(0,1.9,0.1))), color="0.8")

ax.legend([mc,mr,utc,d,area],['MC','MR','UTC','D','Profit ~ 17.56'])
ax.set_ylabel('Price per quantity')
ax.set_xlabel('Quantity (in appropriate units)')

plt.tight_layout()
fig1.savefig('images/sec1_2.png')

# ### figure 4 ###
fig3 = plt.figure(3)
ax = fig3.add_subplot(111)
Q = np.arange(0,2.5,0.1)
MC = 3*Q**2 - 12*Q + 15
UTC = Q**2 - 6*Q + 15
MR = -20*Q + 20
D = -10*Q + 20

mc, = ax.plot(Q,MC, label = 'mc')
mr, = ax.plot(Q,MR, label = 'mr')
utc, = ax.plot(Q,UTC, label = 'utc')
d, = ax.plot(Q,D, label='d')


ax.set_xlim(0,2.5)
ax.set_ylim(0,22)
ax.grid(True, linestyle='--')

eq_x, = ax.plot(0.52+np.zeros(len(np.arange(0,23,1))),np.arange(0,23,1), '--',label = 'eq_x', color = 'r')
eq_y, = ax.plot(np.arange(0,0.53,0.01), 12.15+np.zeros(len(np.arange(0,0.53,0.01))),'--',label = 'eq_y', color = 'b')
eq_y2, = ax.plot(np.arange(0,0.53,0.01), 14.77+np.zeros(len(np.arange(0,0.53,0.01))),'--',label = 'eq_y', color = 'b')
area = plt.fill_between(np.arange(0,0.53,0.01),12.15+np.zeros(len(np.arange(0,0.53,0.01))), 14.77+np.zeros(len(np.arange(0,0.53,0.01))), color="0.8")

ax.legend([mc,mr,utc,d,area],['MC','MR','UTC','D','Profit ~ 1.37'])
ax.set_ylabel('Price per quantity')
ax.set_xlabel('Quantity (in appropriate units)')

plt.tight_layout()
fig3.savefig('images/sec1_4.png')

# ### figure 5 ###
fig5 = plt.figure(5)
ax = fig5.add_subplot(111)
Q = np.arange(0,3.5,0.1)
MC = 3*Q**2 - 12*Q + 15
UTC = Q**2 - 6*Q + 15
MR2 = -20*Q + 20
D2 = -10*Q + 20
MR1 = -16*Q + 32
D1 = -8*Q + 32

mc, = ax.plot(Q,MC, label = 'mc')
mr1, = ax.plot(Q,MR1, label = 'mr1')
utc, = ax.plot(Q,UTC, label = 'utc')
d1, = ax.plot(Q,D1, label='d')
mc, = ax.plot(Q,MC, label = 'mc')
mr2, = ax.plot(Q,MR2, label = 'mr2')
utc, = ax.plot(Q,UTC, label = 'utc')
d2, = ax.plot(Q,D2, label='d')

ax.set_xlim(0,3.5)
ax.set_ylim(0,32)
ax.grid(True, linestyle='--')
ax.legend([mc,mr1,utc,d1,mr2,d2],['MC','MR1','UTC','D1','MR2','D2'])
ax.set_ylabel('Price per quantity')
ax.set_xlabel('Quantity (in appropriate units)')

eq_x, = ax.plot(1.75+np.zeros(len(np.arange(0,33,1))),np.arange(0,33,1), '--',label = 'eq_x', color = 'r')
eq_x2, = ax.plot(0.80+np.zeros(len(np.arange(0,33,1))),np.arange(0,33,1), '--',label = 'eq_x1', color = 'r')
eq_x3, = ax.plot(2.55+np.zeros(len(np.arange(0,33,1))),np.arange(0,33,1), '--',label = 'eq_x2', color = 'r')
eq_y, = ax.plot(np.arange(0,3.6,0.1), 4+np.zeros(len(np.arange(0,3.6,0.1))),'--',label = 'eq_y', color = 'b')

ax.annotate('MR1(Q1)',xy=(1.75,4),xytext=(2,10.5),arrowprops=dict(arrowstyle="->",connectionstyle="angle3"))
ax.annotate('MR2(Q2)',xy=(0.8,4),xytext=(0.1,7),arrowprops=dict(arrowstyle="->",connectionstyle="angle3"))
ax.annotate('MC(Q1+Q2)',xy=(2.55,4),xytext=(2.75,1.9),arrowprops=dict(arrowstyle="->",connectionstyle="angle3"))
plt.tight_layout()
fig5.savefig('images/sec1_5.png')

plt.show()

