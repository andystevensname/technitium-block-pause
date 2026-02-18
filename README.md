# Technitium Block Pause

A Home Assistant custom integration to monitor and control ad blocking on a [Technitium DNS Server](https://technitium.com/dns/).

## Features

- **Switch entity** - Toggle ad blocking on/off directly from Home Assistant
- **Sensor entity** - Shows blocking status (`enabled`, `paused`, or `disabled`) with attributes
- **Services** - Pause, enable, or disable ad blocking via automations
- **Device grouping** - Entities grouped under a Technitium device in the UI
- **Connection validation** - Tests connection during setup

## Installation

### Manual Installation
1. Copy the `technitium_block_pause` folder to your Home Assistant `custom_components` directory
2. Restart Home Assistant
3. Go to **Settings → Devices & Services → Add Integration**
4. Search for "Technitium Block Pause"
5. Enter your Technitium DNS server URL and API token

### HACS (Coming Soon)
This integration may be added to HACS in the future.

## Configuration

| Field | Description | Example |
|-------|-------------|----------|
| Host URL | URL to your Technitium DNS server | `http://192.168.1.100:5380` |
| API Token | Your Technitium API token | Get from Technitium web UI |

### Getting Your API Token
1. Open the Technitium DNS web console
2. Go to **Administration → Sessions**
3. Create a new API token or use an existing session token

## Entities

### Switch: Ad Blocking
- **Entity ID**: `switch.technitium_block_pause_ad_blocking`
- **ON**: Ad blocking is enabled
- **OFF**: Ad blocking is disabled

### Sensor: Blocking Status
- **Entity ID**: `sensor.technitium_block_pause_blocking_status`
- **States**: `enabled`, `paused`, `disabled`, `unknown`
- **Attributes**:
  - `enable_blocking`: Whether blocking is enabled in settings
  - `temporary_disable_until`: Timestamp when temporary pause ends (if paused)

## Services

### `technitium_block_pause.pause_ad_blocking`
Temporarily pause ad blocking for a specified duration.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| duration | int | Yes | Seconds to pause (converted to minutes for Technitium) |

### `technitium_block_pause.enable_ad_blocking`
Enable ad blocking (cancels any temporary pause).

### `technitium_block_pause.disable_ad_blocking`
Disable ad blocking indefinitely.

## Options

After setup, you can configure these options:

| Option | Default | Description |
|--------|---------|-------------|
| Update interval | 30 | Seconds between status polls |
| Pause min | 60 | Minimum pause duration (seconds) |
| Pause max | 86400 | Maximum pause duration (seconds) |
| API timeout | 10 | API request timeout (seconds) |

## Example Dashboard Card

```yaml
type: horizontal-stack
cards:
  - type: button
    name: Enable
    icon: mdi:shield-check
    tap_action:
      action: call-service
      service: technitium_block_pause.enable_ad_blocking
  - type: button
    name: 5 min
    icon: mdi:shield-off
    tap_action:
      action: call-service
      service: technitium_block_pause.pause_ad_blocking
      data:
        duration: 300
  - type: button
    name: Disable
    icon: mdi:shield-off-outline
    tap_action:
      action: call-service
      service: technitium_block_pause.disable_ad_blocking
```

## Links

- [Technitium DNS Server](https://technitium.com/dns/)
- [Technitium API Documentation](https://github.com/TechnitiumSoftware/DnsServer/blob/master/APIDOCS.md)
- [Report Issues](https://github.com/andystevensname/technitium_block_pause/issues)
