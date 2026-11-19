
import math
g=9.81
out=[]
def hdr(s): out.append("\n=== %s ==="%s)

# 2.1
hdr("2.1 Waterfall")
m=2.0; dz=-50.0
dPE=m*g*dz
dKE=-dPE; dU=0.0; dE=dPE+dKE+dU
out.append("1->2 dPE=%.0f J  dKE=%.0f J  dU=%.0f J  dE=%.0f J"%(dPE,dKE,dU,dE))
dPE3=-m*g*50; dKE3=0.0; dU3=-dPE3; dE3=0.0
out.append("1->3 dPE=%.0f  dKE=%.0f  dU=%.0f  dE=%.0f"%(dPE3,dKE3,dU3,dE3))
du=dU3/m; dT=du/4190.0
out.append("du=%.1f J/kg  dT=%.3f K"%(du,dT))

# 2.3
hdr("2.3 Balloon")
patm=1.013e5; dV=0.25
out.append("W_balloon = patm*dV = %.0f J = %.2f kJ"%(patm*dV,patm*dV/1000))
out.append("(60 bar is irrelevant to this boundary work)")

# 2.5
hdr("2.5 SI engine")
V1=1.6e-3; r=9.0; n=1.4; R=287.0; P1=1e5; T1=288.15; T3=3273.15
V2=V1/r
T2=T1*r**(n-1); P2=P1*r**n
m_air=P1*V1/(R*T1)
P3=P2*T3/T2; V3=V2
T4=T3/r**(n-1); P4=P3/r**n; V4=V1
cv=R/(n-1)
W12=m_air*R*(T2-T1)/(1-n); W23=0.0
W34=m_air*R*(T4-T3)/(1-n); W41=0.0
Wnet=W12+W23+W34+W41
Qin=m_air*cv*(T3-T2); Qout=m_air*cv*(T1-T4)
eta=1-1/r**(n-1)
out.append("V2=%.4e m3 (%.3f L)"%(V2,V2*1e3))
out.append("T2=%.1f K  P2=%.2f bar"%(T2,P2/1e5))
out.append("m=%.3e kg (%.2f g)"%(m_air,m_air*1e3))
out.append("V3=%.3f L  P3=%.1f bar  T3=%.0f K"%(V3*1e3,P3/1e5,T3))
out.append("V4=%.3f L  P4=%.2f bar  T4=%.0f K"%(V4*1e3,P4/1e5,T4))
out.append("W12=%.0f J  W23=0  W34=%.0f J  W41=0  Wnet=%.0f J (=%.2f kJ)"%(W12,W34,Wnet,Wnet/1000))
out.append("Qin=%.0f J Qout=%.0f J  eta=%.3f (1-1/r^(n-1))  check eta=%.3f"%(Qin,Qout,eta,Wnet/Qin))
rpm=5000.0; cyc=rpm/60/2
out.append("cycles/s=%.2f  Power=%.1f kW"%(cyc,Wnet*cyc/1000))
pme=Wnet/(V1-V2)
out.append("p_me=%.3e Pa = %.2f bar"%(pme,pme/1e5))
out.append("Wnet/(P1*V1)=%.3f"%(Wnet/(P1*V1)))

# 2.6
hdr("2.6 Vertical cylinder")
A=0.1; mp=203.9; V1b=0.05; P1b=1e5; T1b=26.8+273.15; Rg=290.0; Cv=725.0; patm=1e5
m_g=P1b*V1b/(Rg*T1b)
P2b=patm+mp*g/A
T2b=P2b*V1b/(m_g*Rg)
Q12=m_g*Cv*(T2b-T1b)
W23b=P2b*(A*0.2); V3b=V1b+A*0.2
T3b=P2b*V3b/(m_g*Rg)
Q23=m_g*Cv*(T3b-T2b)+W23b
dU23=m_g*Cv*(T3b-T2b)
out.append("m=%.5f kg  T1=%.2f K"%(m_g,T1b))
out.append("P2=%.1f Pa = %.2f bar"%(P2b,P2b/1e5))
out.append("T2=%.1f K  W12=0  Q12=dU=%.3f kJ"%(T2b,Q12/1000))
out.append("W23=%.3f kJ  V3=%.4f m3  T3=%.1f K  dU23=%.3f kJ  Q23=%.3f kJ"%(W23b/1000,V3b,T3b,dU23/1000,Q23/1000))

# 2.7
hdr("2.7 Cycle")
Q12c=170.0; Q23c=-100.0; W23c=-42.0; Q31=0.0
Qnet=Q12c+Q23c+Q31
W31=Qnet-W23c
out.append("Qnet=%.0f kJ  W31=%.0f kJ"%(Qnet,W31))

print("\n".join(out))

assert abs(dPE+981)<1, "2.1"
assert abs(round(pme/1e5,1)-14.7)<0.2, pme
assert abs(Q23/1000-8.40)<0.02 and abs(W23b/1000-2.40)<0.01
assert abs(T3b-504)<1 and abs(T3b-504)<1
assert abs(Q12/1000-2.50)<0.02
assert abs(W31-112)<1e-6
print("\nALL CHECKS PASSED")
