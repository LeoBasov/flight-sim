import atmosphere
import numpy as np

g = 9.81
    
class Ascend:
	def __init__(self):
		self.atm = atmosphere.Atmosphere()
		self.dt = 1e-2 # s
		self.c_d = 0.04
		self.S = 40
		self.c_e = 2530.98
		self.m_dot = 80
		
		self.m0 = 10000
		self.mf = 6500
		self.nu_b = 0.9
		
		self.m = self.m0 - (1 - self.nu_b)*self.mf
		
		self.a = [0]
		self.v = [0]
		self.h = [0]
		self.t = [0]
		self.q = [0]
		
	def set_ce_m_dot(self, c_e, m_dot):
		self.c_e = c_e
		self.m_dot = m_dot
		
	def set_mass(self, m0, mf, nu_b):
		self.m0 = m0
		self.mf = mf
		self.nu_b = nu_b
		self.m = self.m0 - (1 - self.nu_b)*self.mf
		
	def set_cd_S(self, c_d, S):
		self.c_d = c_d
		self.S = S
		
	def run(self):
		self.m = self.m0 - (1 - self.nu_b)*self.mf
		m_dot = self.m_dot
        
		self.a = [0]
		self.v = [0]
		self.h = [0]
		self.t = [0]
		self.q = [0]
        
		while True:           
			T = self.c_e * m_dot
			D = self.drag(self.h[-1], self.v[-1], self.S, self.c_d)
			self.m -= self.dt*m_dot
    
			self.t.append(self.t[-1] + self.dt)
			self.a.append(T/self.m - D/self.m - g)
			self.h.append(self.h[-1] + self.dt*self.v[-1] + 0.5*self.a[-1]*self.dt*self.dt)
			self.v.append(self.v[-1] + self.dt*self.a[-1])
			self.q.append(0.5*self.atm.rho(self.h[-1])*self.v[-1]**2)
    		
			if self.h[-1] < self.h[-2]:
				break
			elif self.m <= (self.m0 - self.mf):             
				m_dot = 0.0
                
		self.k = 100000*np.ones(len(self.t))
		
	def drag(self, h, v, S, c_d):
		return S * c_d * 0.5*self.atm.rho(h)*v**2
