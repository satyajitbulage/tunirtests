import subprocess

def system(cmd):
    """
    Invoke a shell command.

    :returns: A tuple of output, err message, and return code
    """
    ret = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE,
                stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)
    out, err = ret.communicate()
    return out, err, ret.returncode


def if_atomic():
    "Tries to identify atomic image."
    out, err, eid = system('which rpm-ostree')
    if eid != 0:
        return False
    return True

def if_upgrade():
    "Check for available ostree upgrade for host."
    out, err, eid = system('sudo atomic host upgrade --check')
    if eid != 0:
        return False
    return True

def if_rollback():
    "Check for available rollback target for host."
    out, err, eid = system('sudo atomic host status -p')
    out = out.decode('utf-8')
    if "ROLLBACK TARGET" in out:
        return True
    return False
