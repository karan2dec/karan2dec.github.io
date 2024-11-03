require 'liquid'

module Jekyll
  def titlecase(input)
    input.split.map(&:capitalize).join(' ')
  end
end

Liquid::Template.register_filter(Jekyll)
