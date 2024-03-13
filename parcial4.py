def alg_descuento():
    cons_errostr = 'Debes seleccionar una opción válida'
    cons_desc1str = 'Tiene un descuento del 08%'
    cons_desc2str = 'Tiene un descuento del 05%'
    cons_desc3str = 'Tiene un descuento del 15%'
    cons_desc4str = 'Tiene un descuento del 12%'
    cons_desc5str = 'Tiene un descuento del 10%'
    print('Ingrese precio del producto:')
    var_precio = float(input())
    print('Seleccione el producto:')
    print('1. Alimentos\n2. Aseo\n3. Seguridad\n4. Electrodomesticos\n5. Ferreteria')
    var_tipo = int(input())

    if var_tipo < 1 or var_tipo > 3:
        print(cons_errostr)
        return

    if var_tipo == 1:
        var_descuento = var_precio * 0.08
        print(cons_desc1str)
    elif var_tipo == 2:
        var_descuento = var_precio * 0.05
        print(cons_desc2str)
    elif var_tipo == 3:
        var_descuento = var_precio * 0.15
        print(cons_desc3str)
    elif var_tipo == 4:
        var_descuento = var_precio * 0.12
        print(cons_desc4str)
    else:
        var_descuento = var_precio * 0.10
        print(cons_desc5str)

    print('      Reporte de factura      ')
    print('...............................')
    print('Precio...............$', var_precio)
    print('Descuento............$', var_descuento)
    print('Total................$', (var_precio - var_descuento))

alg_descuento()