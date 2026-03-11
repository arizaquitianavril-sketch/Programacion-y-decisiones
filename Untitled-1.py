# %%
# =============================================================================
# SCRIPT: CALCULADORA FINANCIERA DE DIVISAS PARA ECONOMISTAS
# =============================================================================

# 1. BIENVENIDA E INTERACCIÓN INICIAL
# Mostramos un encabezado estético para que el usuario sepa qué hace el programa.
print("==========================================================")
print("🏦 BIENVENIDO A LA CALCULADORA DE DIVISAS ACADÉMICA 💹")
print("Diseñada para el análisis de mercados internacionales")
print("==========================================================\n")

# Iniciamos un bloque 'try' (intentar) para capturar posibles errores de escritura.
try:
    
    # 2. ENTRADAS DE DATOS (INPUTS & CASTING)
    # El comando 'input' recibe texto. Usamos 'float()' para convertir ese texto
    # en un número decimal. Nota: En finanzas usamos float para permitir decimales.
    
    # Solicitamos el capital base en Pesos Colombianos.
    cop_disponibles = float(input("💰 Ingresa la cantidad de Pesos Colombianos (COP): "))
    
    # Solicitamos la TRM (Tasa Representativa del Mercado) del Dólar actual.
    tasa_dolar = float(input("🇺🇸 Ingresa la tasa de cambio del Dólar (USD): "))
    
    # Solicitamos la tasa de cambio para el Euro.
    tasa_euro = float(input("🇪🇺 Ingresa la tasa de cambio del Euro (EUR): "))

    # 3. PROCESAMIENTO (CÁLCULOS)
    # La lógica económica básica: Dividimos el capital por el valor de la divisa.
    # Almacenamos el resultado en nuevas variables con nombres descriptivos.
    
    conversion_usd = cop_disponibles / tasa_dolar # Cálculo para Dólares
    conversion_eur = cop_disponibles / tasa_euro  # Cálculo para Euros

    # 4. SALIDA DE INFORMACIÓN (OUTPUTS)
    # Usamos f-strings (f"") para mezclar texto y variables de forma elegante.
    # El formato ':,.2f' pone separadores de miles y limita a 2 decimales exactos.
    
    print("\n" + "-"*40)
    print("📊 RESUMEN DE LA CONVERSIÓN")
    print("-"*40)
    
    # Mostramos el monto original formateado.
    print(f"💵 Monto original: ${cop_disponibles:,.2f} COP")
    
    # Mostramos el equivalente en Dólares con emoji de bandera.
    print(f"🇺🇸 Equivalente en Dólares: ${conversion_usd:,.2f} USD")
    
    # Mostramos el equivalente en Euros con emoji de bandera.
    print(f"🇪🇺 Equivalente en Euros:   €{conversion_eur:,.2f} EUR")
    
    print("-"*40)
    print("✅ Proceso completado exitosamente.")

# GESTIÓN DE ERRORES:
# Si el usuario escribe letras en lugar de números, el programa no "muere",
# sino que ejecuta este bloque de advertencia.
except ValueError:
    print("\n" + "!"*40)
    print("⚠️  ERROR DE ENTRADA DE DATOS")
    print("❌ Por favor, ingresa solo números (usa punto para decimales).")
    print("❌ No uses letras ni caracteres especiales en los montos.")
    print("!"*40)

finally:
    # Este mensaje se muestra siempre para cerrar la interacción.
    print("\nFin del reporte financiero.")

