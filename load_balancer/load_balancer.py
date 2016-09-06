from machine_pool import MachinePool

pool = MachinePool('server_image')
sessions = []
try:
    for i in range(3):
        sessions.append(pool.acquire("batman", "123"))
        a = 0

    # You now have three running machines.
    for session in sessions:
        with session.guest.create_session("batman", "123") as gs:
            _, out, _ = gs.execute("ifconfig")
            print(out)
except Exception, e:
    print(e)
finally:
    for session in sessions:
        try:
            pool.release(session)
        except Exception as err:
            print("Error raised on release: %s" % err)
