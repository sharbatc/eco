import matplotlib.pyplot as plt 
import numpy as np

### figure 0 ###
fig0 = plt.figure(0)
ax = fig0.add_subplot(111)
Q_D = np.arange(0.5,15,1)
P_D = -Q_D + 15

Q_S = np.arange(0.5,10,1)
P_S = Q_S + 5

demand, = ax.plot(Q_D,P_D, label = 'demand')
supply, = ax.plot(Q_S,P_S, label = 'supply')

eq_x, = ax.plot(5+np.zeros(11),np.arange(0,11,1), '--',label = 'eq_x', color = 'r')
eq_y, = ax.plot(np.arange(0,6,1), 10+np.zeros(6),'--',label = 'eq_y', color = 'r')

ax.set_ylim(0,15)
ax.set_xlim(0,15)
ax.grid(True, linestyle='--')
ax.legend([demand, supply],['Demand','Supply'])
ax.set_ylabel('Price per quantity (in CHF)')
ax.set_xlabel('Quantity (in appropriate units)')

ax.annotate('(5, 10)',xy=(5,10),xytext=(8,9),arrowprops=dict(arrowstyle="->",connectionstyle="angle3"))
ax.set_xticks([5],minor=True)
ax.set_xticklabels('5',color='r',minor=True)
yticks = ax.yaxis.get_major_ticks()
yticks[5].label.set_color('r')

plt.tight_layout()
fig0.savefig('images/sec1_1.png')

### figure 1 again ###

fig1 = plt.figure(1)
ax = fig1.add_subplot(111)

Q_D = np.arange(0.5,15,1)
P_D = -Q_D + 15
TC = P_D*Q_D

Q_S = np.arange(0.5,10,1)
P_S = Q_S + 5
TR = P_S*Q_S

tr, = ax.plot(Q_S,TR, label = 'tr')
texp, = ax.plot(Q_D,TC, label = 'texp')
ax.set_ylim(0,145)
ax.set_xlim(0,15)
ax.grid(True, linestyle='--')
ax.legend([tr, texp],['Revenue','Expenditure'])
ax.set_ylabel('Price per quantity (in CHF)')
ax.set_xlabel('Quantity (in appropriate units)')

plt.tight_layout()
fig1.savefig('images/sec1_2.png')
#### figure 2 ###

fig2 = plt.figure(2)
ax = fig2.add_subplot(111)
demand, = ax.plot(Q_D,P_D, label = 'demand')
supply, = ax.plot(Q_S,P_S, label = 'supply')

eq_x, = ax.plot(1+np.zeros(7),np.arange(0,7,1), '--',label = 'eq_x', color = 'r')
eq_y, = ax.plot(np.arange(0,10,1), 6+np.zeros(10),'--',label = 'eq_y', color = 'r')
eq_x, = ax.plot(9+np.zeros(7),np.arange(0,7,1), '--',label = 'eq_x', color = 'r')


ax.set_ylim(0,15)
ax.set_xlim(0,15)
ax.grid(True, linestyle='--')
ax.legend([demand, supply],['Demand','Supply'])
ax.set_ylabel('Price per quantity (in CHF)')
ax.set_xlabel('Quantity (in appropriate units)')

ax.annotate('(1, 6)',xy=(1,6),xytext=(3.5,4.5),arrowprops=dict(arrowstyle="->",connectionstyle="angle3"))
ax.annotate('(9, 6)',xy=(9,6),xytext=(7.5,4.5),arrowprops=dict(arrowstyle="->",connectionstyle="angle3"))
ax.set_xticks([1,9],minor=True)

yticks = ax.yaxis.get_major_ticks()
yticks[3].label.set_color('r')

plt.tight_layout()
fig2.savefig('images/sec2_1.png')
#### figure 3 #####

fig3 = plt.figure(3)
ax = fig3.add_subplot(111)
Q_D = np.arange(0.5,15,1)
P_D = -Q_D + 16

Q_S = np.arange(0.5,10,1)
P_S = Q_S + 5

demand, = ax.plot(Q_D,P_D, label = 'demand')
supply, = ax.plot(Q_S,P_S, label = 'supply')

ax.set_ylim(0,15)
ax.set_xlim(0,15)
ax.grid(True, linestyle='--')
ax.legend([demand, supply],['Demand','Supply'])
ax.set_ylabel('Price per quantity (in CHF)')
ax.set_xlabel('Quantity (in appropriate units)')

for q in np.arange(5,6,0.01):
	p_d = -q + 16
	p_s = q + 5
	if np.abs(p_d - p_s) < 0.0001 :
		break
p = q + 5


eq_x, = ax.plot(q+np.zeros(np.int(p)+2),np.arange(0,np.int(p)+2,1), '--',label = 'eq_x', color = 'r')
eq_y, = ax.plot(np.arange(0,np.int(q)+2,1), p+np.zeros(np.int(q)+2),'--',label = 'eq_y', color = 'r')

ax.annotate('(5.5 , 10.5)',xy=(5.5,10.5),xytext=(7.5,11.5),arrowprops=dict(arrowstyle="->",connectionstyle="angle3"))
plt.tight_layout()
fig3.savefig('images/sec3_1.png')

### fig 4 ###

fig4 = plt.figure(4)
ax = fig4.add_subplot(111)
Q_D = np.arange(0.5,15,1)
P_D = -Q_D + 15

Q_S = np.arange(0.5,10,1)
P_S = Q_S + 3

demand, = ax.plot(Q_D,P_D, label = 'demand')
supply, = ax.plot(Q_S,P_S, label = 'supply')

ax.set_ylim(0,15)
ax.set_xlim(0,15)
ax.grid(True, linestyle='--')
ax.legend([demand, supply],['Demand','Supply'])
ax.set_ylabel('Price per quantity (in CHF)')
ax.set_xlabel('Quantity (in appropriate units)')

for q in np.arange(5,6,0.01):
	p_d = -q + 15
	p_s = q + 3
	if np.abs(p_d - p_s) < 0.0001 :
		break
p = q + 3


eq_x, = ax.plot(q+np.zeros(np.int(p)+2),np.arange(0,np.int(p)+2,1), '--',label = 'eq_x', color = 'r')
eq_y, = ax.plot(np.arange(0,np.int(q)+2,1), p+np.zeros(np.int(q)+2),'--',label = 'eq_y', color = 'r')
eq_y, = ax.plot(np.arange(0,np.int(q)+3,1), 10+np.zeros(np.int(q)+3),'--',label = 'eq_y', color = 'r')
ax.annotate('(6 , 9)',xy=(6,9),xytext=(8.5,7.2),arrowprops=dict(arrowstyle="->",connectionstyle="angle3"))

plt.tight_layout()
fig4.savefig('images/sec4_1.png')
### figure 5 ###

fig5 = plt.figure(5)
ax = fig5.add_subplot(121)

Q_TC = np.arange(0,1000,100)
Q_TC = np.insert(Q_TC,8,750)
TC = np.asarray([400 ,1000 ,1300 ,1500 ,1600 ,1700 ,1850 ,2200 ,2400 ,2650 ,3600])

Q_TR = np.arange(0,1000,100)
Q_TR = np.insert(Q_TR,8,750)
TR = 4*Q_TR

tc, = ax.plot(Q_TC,TC, 'o-', label = 'tc')
tr, = ax.plot(Q_TR,TR, label = 'tr')

ax.set_xlim(-10,1000)
ax.set_ylim(0,3700)
ax.set_xlabel('Quantity of medicine')
ax.set_ylabel('Total Cost / Total Revenue')
ax.grid(True, linestyle='--')
ax.legend([tc, tr],['Total Cost','Total Revenue'])
eq_x, = ax.plot(700+np.zeros(29),np.arange(0,2900,100), '--',label = 'eq_x', color = 'r')
ax.annotate('(400,1600)',xy=(400,1600),xytext=(500,1200),arrowprops=dict(arrowstyle="->",connectionstyle="angle3"))
ax.annotate('(900,3600)',xy=(900,3600),xytext=(700,3200),arrowprops=dict(arrowstyle="->",connectionstyle="angle3"))
profit_array = np.array([])
for quantity in np.arange(1,900,1):
	TR_calc = 4*quantity
	id_left = np.searchsorted(Q_TC,quantity)
	TC_calc = TC[id_left-1] + ((TC[id_left] - TC[id_left-1])/(Q_TC[id_left] - Q_TC[id_left-1]))*(quantity-Q_TC[id_left-1]) 
	profit = TR_calc - TC_calc
	profit_array = np.append(profit_array,profit)

profit_array = np.append(profit_array,0)
ax2 = fig5.add_subplot(122)
profit, = ax2.plot(profit_array, label = 'profit')
ax2.set_xlim(-10,1000)
ax2.set_xlabel('Quantity of medicine')
ax2.set_ylabel('Profit')
ax2.grid(True, linestyle='--')
eq_x, = ax2.plot(np.arange(0,1000,100),650+np.zeros(10), '--',label = 'eq_x', color = 'r')
eq_x, = ax2.plot(np.arange(0,1000,100),np.zeros(10), '--',label = 'eq_x', color = 'r')
ax2.annotate('(~700,650)',xy=(700,650),xytext=(300,500),arrowprops=dict(arrowstyle="->",connectionstyle="angle3"))

## figure 6 ##
fig6 = plt.figure(6)
ax = fig6.add_subplot(111)

Q_TC = np.arange(0,1000,100)
Q_TC = np.insert(Q_TC,8,750)

TC = np.asarray([400 ,1000 ,1300 ,1500 ,1600 ,1700 ,1850 ,2200 ,2400 ,2650 ,3600],dtype=float)
MC = np.divide(np.append(np.diff(TC),0),np.append(np.diff(Q_TC),0)) #diff deletes an element


ax.set_xlabel('Quantity of medicine')
ax.set_ylabel('Marginal Cost')
ax.grid(True, linestyle='--')

mc, = ax.plot(Q_TC,MC, 'o-', label = 'mc')
mr, = ax.plot(Q_TC,4+np.zeros(11),label = 'mr')
ax.set_xlim(0,1000)
ax.set_ylim(0,10)
ax.set_xlabel('Quantity of medicine')
ax.set_ylabel('Marginal Cost / Marginal Revenue')
ax.grid(True, linestyle='--')
ax.legend([mc, mr],['Marginal Cost','Marginal Revenue'])
eq_x, = ax.plot(700+np.zeros(10),np.arange(0,4.5,0.45), '--',label = 'eq_x', color = 'r')


plt.tight_layout()
fig6.savefig('images/pol3_1.png')


## figure 7 ##


fig7 = plt.figure(7)
ax = fig7.add_subplot(111)

Q_TC = np.arange(0,1000,100)
Q_TC = np.insert(Q_TC,8,750)
TC = np.asarray([400 ,1000 ,1300 ,1500 ,1600 ,1700 ,1850 ,2200 ,2400 ,2650 ,3600])

Q_TR = np.arange(0,1000,100)
Q_TR = np.insert(Q_TR,8,750)
TR = 4.5*Q_TR
TR_old = 4*Q_TR

tc, = ax.plot(Q_TC,TC, 'o-', label = 'tc')
tr, = ax.plot(Q_TR,TR, label = 'tr')
tr_old, = ax.plot(Q_TR,TR_old, label = 'tr_old')

ax.set_xlim(-10,1000)
ax.set_ylim(0,4000)
ax.set_xlabel('Quantity of medicine')
ax.set_ylabel('Total Cost / Total Revenue')
ax.grid(True, linestyle='--')
ax.legend([tc, tr,tr_old],['Total Cost','Total Revenue','Old Total Revenue'])

# eq_x, = ax.plot(700+np.zeros(29),np.arange(0,2900,100), '--',label = 'eq_x', color = 'r')
ax.annotate('(342,1539)',xy=(342,1539),xytext=(500,1200),arrowprops=dict(arrowstyle="->",connectionstyle="angle3"))
# ax.annotate('(900,3600)',xy=(900,3600),xytext=(700,3200),arrowprops=dict(arrowstyle="->",connectionstyle="angle3"))
profit_array = np.array([])

for quantity in np.arange(1,900,1):
	TR_calc = 4.5*quantity
	id_left = np.searchsorted(Q_TC,quantity)
	TC_calc = TC[id_left-1] + ((TC[id_left] - TC[id_left-1])/(Q_TC[id_left] - Q_TC[id_left-1]))*(quantity-Q_TC[id_left-1]) 
	profit = TR_calc - TC_calc
	profit_array = np.append(profit_array,profit)

profit_array = np.append(profit_array,0)
equilibrium_point = np.searchsorted(profit_array,0)


x_hatch = np.insert(Q_TC[4:],0,342)
y1_hatch = np.insert(TC[4:],0,1539)
y2_hatch = np.insert(TR[4:],0,1539)
y3_hatch = TR_old[4:]

plt.fill_between(x_hatch, y1_hatch, y2_hatch, color="0.6")
plt.fill_between(Q_TC[4:], TC[4:], y3_hatch, color="0.6",hatch = '-')

plt.tight_layout()
fig7.savefig('images/pol4.png')


### figure 8 ###

fig8 = plt.figure(8)
ax = fig8.add_subplot(111)

Q_TC = np.arange(0,1000,100)
Q_TC = np.insert(Q_TC,8,750)
TC = np.asarray([400 ,1000 ,1300 ,1500 ,1600 ,1700 ,1850 ,2200 ,2400 ,2650 ,3600])
TC_new = TC-200
Q_TR = np.arange(0,1000,100)
Q_TR = np.insert(Q_TR,8,750)
TR = 4*Q_TR

tc, = ax.plot(Q_TC,TC, 'o-', label = 'tc')
tc_new, = ax.plot(Q_TC, TC_new, label = 'tc_new')
tr, = ax.plot(Q_TR,TR, label = 'tr')
ax.set_xlim(-10,1000)
ax.set_ylim(0,4000)
ax.set_xlabel('Quantity of medicine')
ax.set_ylabel('Total Cost / Total Revenue')
ax.grid(True, linestyle='--')
ax.legend([tc, tc_new, tr],['Total Cost','New Total Cost','Total Revenue'])

profit_array=np.array([])
for quantity in np.arange(1,900,1):
	TR_calc = 4*quantity
	id_left = np.searchsorted(Q_TC,quantity)
	TC_calc = TC_new[id_left-1] + ((TC_new[id_left] - TC_new[id_left-1])/(Q_TC[id_left] - Q_TC[id_left-1]))*(quantity-Q_TC[id_left-1]) 
	profit = TR_calc - TC_calc
	profit_array = np.append(profit_array,profit)

profit_array = np.append(profit_array,0)
equilibrium_point = np.searchsorted(profit_array,0,side='left')

ax.annotate('(333,1332)',xy=(333,1332),xytext=(500,1100),arrowprops=dict(arrowstyle="->",connectionstyle="angle3"))

x_hatch = np.insert(Q_TC[4:],0,333)
y1_hatch = np.insert(TC_new[4:],0,1332)
y2_hatch = np.insert(TC[4:],0,1332)
plt.fill_between(x_hatch, y1_hatch, y2_hatch, color="0.6")
plt.tight_layout()
fig8.savefig('images/pol5.png')

plt.show()

