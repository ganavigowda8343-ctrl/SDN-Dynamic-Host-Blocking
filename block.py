from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

blocked_mac = "00:00:00:00:00:01"

def _handle_ConnectionUp(event):
    log.info("Switch connected")

def _handle_PacketIn(event):
    packet = event.parsed
    if not packet.parsed:
        return

    if str(packet.src) == blocked_mac:
        log.info("Blocking %s", packet.src)
        return

    msg = of.ofp_packet_out()
    msg.data = event.ofp
    msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
    event.connection.send(msg)

def launch():
    core.openflow.addListenerByName("ConnectionUp", _handle_ConnectionUp)
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
