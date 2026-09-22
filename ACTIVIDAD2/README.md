# **Actividad de Clase No. 2:**
# Firma y Verificación de mensajes mediante el protocolo RSA

## Procedimiento

### **1. Creación de claves pública y privada según RSA:**

*i.* Seleccione dos valores $p$ y $q$ primos, tal que:

   $$
   p,q \in (36,50)
   $$

*ii.* Calcule:

   $$
   n=p\cdot q
   $$

*iii.* Calcule la **Función de Euler**:

   $$
   \varphi(n)
   $$

*iv.* Seleccione un valor $e$ primo, menor que $\varphi(n)$:

   $$
   e<\varphi(n)
   $$

*v.* Escriba su **clave pública**:

   $$
   \boxed{K_{\text{pública}}=(n,e)}
   $$

*vi.* Calcule su clave privada, de manera que:

   $$
   e\cdot d\equiv1\pmod{\varphi(n)}
   $$

   * Utilice el [**Algoritmo de Euclides Extendido**](https://github.com/gpatigno/DISCRETAS_2026-2/blob/main/ACTIVIDAD2/Euclides_2026-2.py) para el cálculo de este $d$.


*vii.* Escriba su **clave privada**:

   $$
   \boxed{K_{\text{privada}}=(n,d)}
   $$

---

### **2. Firma Digital:**

*i.* Entre usted y sus compañeros, seleccionen una **fecha de cumpleaños (mes y día)** que permita obtener un número entero:

$$
M= \Box_{mes}\Box_{mes}\Box_{dia}\Box_{dia}
$$

*ii.* Este número será el **mensaje o documento que queremos firmar**.

*iii.* Firme digitalmente su mensaje o documento utilizando su **clave privada**, mediante la operación:

   $$
   m=M^d\bmod n
   $$

*iv.* El valor $m$ será el **documento firmado digitalmente**.

---

### **3. Verificación de firma digital:**

Para verificar un documento firmado por otra persona, se realiza la operación:

   $$
      m'_{\text{Alice}} = m_{\text{Alice}}^{e_{\text{Alice}}} \bmod n_{\text{Alice}}
   $$

donde:

* $(n_{\text{Alice}},e_{\text{Alice}})$ es la **clave pública** de la otra persona.
* $m_{\text{Alice}}$ es el **documento firmado digitalmente**.
* $m'_{\text{Alice}}$ es el **documento recuperado después de la verificación**.

Finalmente, se verifica que:

$$
\boxed{m'_{\text{Alice}}=M_{\text{Alice}}}
$$

Si ambos valores coinciden, la operación de verificación confirma que el mensaje recuperado corresponde al mensaje original bajo el esquema RSA utilizado en el ejercicio.


### **3. Hash criptográfico para cada mensaje:**

Puede utilizar la siguiente calculadora *online*, para el cálculo del **SHA-1** de un cierto mensaje alfanumérico:

* https://xorbin.com/tools/sha1-hash-calculator