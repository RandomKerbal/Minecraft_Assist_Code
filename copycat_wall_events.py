for i in range(4):
    for ii in range(4):
        if i == ii == 0:
            continue
        else:
            print(f'"conn_z{i}x{ii}"' + ':{"add":{"component_groups":[' + f'"conn_yz{i}x{ii}"' + ']}},')
