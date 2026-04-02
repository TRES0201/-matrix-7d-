# setup_matrix.py - Crea todo el universo MATRIX 7D
# Ejecuta esto una sola vez para generar las 14 carpetas

import json
import datetime
from pathlib import Path

# La estructura completa de 14 carpetas
ESTRUCTURA = {
    "01_CODICE_7D": ["Codice_7D_v1.0.md", "versiones_historicas", "traducciones"],
    "02_SP_7D": ["modulo_agora_7d", "modulo_arete_7d", "integracion"],
    "03_TENSOR_PROMETEO": ["tensor_7d.py", "espejo_7d.py", "notario_7d.py", "vigia_7d.py", "simulaciones"],
    "04_CONTRATOS_Y_LEGAL": ["LUL_C7D_1.0.md", "NDA_7D.md", "ToS_SP_7D.md", "firmados", "registros"],
    "05_PROTECCION_Y_DERECHOS": ["notario_7d_config.json", "licencias_activas.json", "violaciones_detectadas.json", "arbitraje"],
    "06_CLIENTES_Y_USUARIOS": ["prospectos.csv", "activos", "inactivos", "silencios_criticos"],
    "07_METRICAS_Y_REPORTES": ["reportes_diarios", "reportes_semanales", "reportes_mensuales"],
    "08_BUCLE_Y_EVOLUCION": ["bucle_principal.py", "auto_revision.py", "enmiendas_codice", "bitacora_cambios.json"],
    "09_AGENTES_AUTONOMOS": ["vigia_7d.py", "notario_7d.py", "espejo_7d.py", "cron_jobs", "workflows"],
    "10_DOCUMENTACION_Y_GUIAS": ["guia_arquitecto.md", "guia_presidente.md", "guia_ministro.md", "api_documentation.html"],
    "11_HERRAMIENTAS_Y_SCRIPTS": ["backup_script.py", "encriptar_archivos.py", "generar_reportes.py", "templates"],
    "12_RESPALDOS_Y_SEGURIDAD": ["diarios", "semanales", "mensuales", "encriptados"],
    "13_EXPANSION_Y_FRONTERAS": ["paises", "sectores", "roadmap_expansion.md"],
    "14_EL_BUQUE_DEL_ARQUITECTO": ["diario_personal.md", "lecciones_aprendidas.md", "errores_cometidos.md", "metas_semanales.md"]
}

def crear_estructura(base_path):
    """Crea toda la estructura de carpetas y archivos base"""
    print("🌌 Creando universo MATRIX 7D...")
    print("="*50)
    
    for carpeta, contenido in ESTRUCTURA.items():
        path = Path(base_path) / carpeta
        path.mkdir(parents=True, exist_ok=True)
        print(f"✅ {carpeta}")
        
        for item in contenido:
            item_path = path / item
            if "." not in item:  # es subcarpeta
                item_path.mkdir(exist_ok=True)
                print(f"   📁 {item}")
            else:  # es archivo
                if not item_path.exists():
                    item_path.touch()
                    # Agregar contenido base a archivos importantes
                    if item == "diario_personal.md":
                        with open(item_path, "w") as f:
                            f.write(f"""# Diario del Arquitecto

## Iniciado: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}

---

## Registro diario

### [Fecha]

**Decisión importante:**

**Dimensión que revisé:**

**Lección aprendida:**

---
""")
                    elif item == "notario_7d_config.json":
                        with open(item_path, "w") as f:
                            json.dump({
                                "version": "1.0",
                                "fecha_creacion": str(datetime.datetime.now()),
                                "activo": True,
                                "alertas": {
                                    "telegram": False,
                                    "email": False
                                }
                            }, f, indent=2)
                    elif item == "bitacora_cambios.json":
                        with open(item_path, "w") as f:
                            json.dump([], f, indent=2)
                    elif item == "prospectos.csv":
                        with open(item_path, "w") as f:
                            f.write("nombre,email,sector,fecha_contacto,estado\n")
                    print(f"   📄 {item}")
    
    print("="*50)
    print("✅ UNIVERSO MATRIX 7D CREADO")
    print(f"📁 Ubicación: {base_path}")
    print("📊 14 carpetas principales")
    print("🔢 50+ subcarpetas y archivos")
    return base_path

if __name__ == "__main__":
    import sys
    
    # Si se pasa un argumento, úsalo como ruta base
    if len(sys.argv) > 1:
        base = sys.argv[1]
    else:
        base = "./MATRIX_DEL_ARQUITECTO_7D"
    
    crear_estructura(base)
