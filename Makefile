sync:
	rsync -avz --exclude='__pycache__' --exclude='.git' --exclude='.vscode' --exclude='*.log' --exclude='*.pyc' . cat@catpi.local:/opt/catai
	ssh cat@catpi.local "sudo systemctl restart catai" || echo done

stop:
	ssh cat@catpi.local "sudo systemctl stop catai" || echo done

status:
	ssh cat@catpi.local "sudo systemctl status catai" || echo done

start:
	ssh cat@catpi.local "sudo systemctl restart catai" || echo done

log-tail:
	ssh cat@catpi.local "journalctl -u catai -f" || echo done

log:
	ssh cat@catpi.local "journalctl -u catai" || echo done



