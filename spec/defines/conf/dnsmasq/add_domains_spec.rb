require 'spec_helper'

describe 'dnsmasq', :type => :define do
  let(:title) {'dnsmasq_conf'}
  let(:params) {{
    :ip => '1.2.3.4.',
    :domains => ['bob.com',
		'alice.com']
  }}

  it { is_expected.to create_file('/etc/dnsmasq.conf') }
end
