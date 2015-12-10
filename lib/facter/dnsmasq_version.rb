#dnsmasq_version.rb

Facter.add(:dnsmasq_version) do
  setcode do
    Facter::Core::Execution.exec('/usr/bin/dnsmasq -v')
  end
end
